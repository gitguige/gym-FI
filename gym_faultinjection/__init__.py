from gym.envs.registration import register

register(
    id='faultinjection-v0',
    entry_point='gym_faultinjection.envs:FIEnv',
    max_episode_steps=350,
)
