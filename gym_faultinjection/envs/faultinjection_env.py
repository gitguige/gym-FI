import os,time
import math

import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FIEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.action_file = "../shared_files/Action.txt"
    self.state_file = "../shared_files/State.txt"

    self.min_position = -50 #related to leading vehicle = dis_lead - dis_control
    self.max_position = 105
    self.max_speed = 14 #related to leading vehicle = vel_control - vel_lead
    self.min_speed = -27

    self.low = np.array([self.min_position, self.min_speed])
    self.high = np.array([self.max_position, self.max_speed])

    self.viewer = None

    self.action_space = spaces.Discrete(3)
    self.observation_space = spaces.Box(self.low, self.high, dtype=np.float32)

    self.seed()

  def seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]

  def step(self, action):
    # cmd = "python /home/uva-dsa/Research/random_injection/1_openpilot_LVSpConst_WOdocker_exponential/run.py /home/uva-dsa/Research/random_injection/1_openpilot_LVSpConst_WOdocker_exponential/fault_library/scenario_5"
    # os.system(cmd)
    assert action<5 and action>=0
    self.write_to_file(self.action_file,int(action))
    time.sleep(.1) #wait for a moment

    #*******read state from file saved by simulators****************#
    fp_state = open(self.state_file,'r')
    line = fp_state.readline()
    line = line.replace('\n',',')
    lineseg = line.split(',')
    fp_state.close()

    assert len(lineseg)>= 3
    done = int(lineseg[0])  #0: None 1; hazard happens
    position = float(lineseg[1])
    velocity = float(lineseg[2])

    self.state = (position, velocity)
    reward = 2*velocity - position

    return np.array(self.state), reward, done, {}
    
  def reset(self):
    print("Reset faultinjection-v0.")
    # print(os.getcwd())
    self.state = np.array([self.np_random.uniform(low=-0.6, high=-0.4), 0])
    return np.array(self.state)
  
  def render(self, mode='human'):
    print("this is faultinjection-v0")

  def close(self):
    print("Close faultinjection-v0")

  '''
  input: file path e.g., "../shared_files/Simulator_start_status.txt"
  return: status 0:stop or wait 1: start
  '''
  def read_status(self, file):
    # print(os.getcwd(),file)
    fp = open(file,'r')
    line = fp.readline()
    start_status = int(line.replace('\n',''))
    fp.close()

    return start_status

  def write_to_file(self, file,info):
    fp = open(file,'r+')
    line = str(info)
    fp.write(line) #save in the file
    fp.close()
