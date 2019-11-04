## This is the environment of faultinjection experiment. 

To install this envirmont please first install the `openai gym`:

```bash
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
cd ..
```

Then copy gym_FI to the same directory of openai gym
```bash
git clone https://github.com/gitguige/gym-FI.git
cd gym-FI
pip install -e .
cd ..
```

Now  you can create an instance of the environment with 
```
gym.make('gym_faultinjection:faultinjection-v0')
```