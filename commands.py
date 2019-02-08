# Install virtualenv using pip
# pip install virtualenv
# ERROR: The executable /Users/jaimealmeida/Repos/rl_projects/rl/bin/python is not functioning
# ERROR: It thinks sys.prefix is '/Users/jaimealmeida/Repos/rl_projects' (should be '/Users/jaimealmeida/Repos/rl_projects/rl')
# ERROR: virtualenv is not compatible with this system or executable
conda install virtualenv

# Create a virtualenv
virtualenv rl_projects

# Activate virtualenv
source rl_projects/bin/activate

# pip install the required packages
(rl_projects) $ pip install -r requirements.txt

sudo pip install gym
pip install ipykernel
ipython kernel install --user --name=projectname
# https://anbasile.github.io/programming/2017/06/25/jupyter-venv/

# http://mckinziebrandon.me/TensorflowNotebooks/2016/12/21/openai.html

# https://stackoverflow.com/questions/52726475/display-openai-gym-in-jupyter-notebook-only

pip install matplotlib
pip install JSAnimation



import gym
environment = gym.make('CartPole-v0')
environment.reset()

# start an iteration and render the environment
for dummy in range(100):
    environment.render()
    environment.step(environment.action_space.sample())


environment = gym.make('SpaceInvaders-v0')
environment = gym.make('Copy-v0')
environment = gym.make('Humanoid-v2')
environment = gym.make('HandManipulateBlock-v0')


The problem is set up as a reinforcement learning problem, with a trial and error method. The environment is described using state_valuesstate_values (?), and the state_values are changed by actions. The actions are determined by an algorithm, based on the current state_value, in order to achieve a particular state_value that is termed a Markov model. In an ideal case, the past state_values does have an influence on future state_values, but here, we assume that the current state_value has all of the previous state_values encoded. There are two types of state_values; one is observable, and the other is non-observable. The model has to take non-observable state_values into account, as well. That is called a Hidden Markov model.
