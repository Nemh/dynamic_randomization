import gym

class RandomizedEnvironment:
    """ Randomized environment class """
    def __init__(self, experiment, parameter_ranges, goal_range):
        self._experiment = experiment
        self._parameter_ranges = parameter_ranges
        self._goal_range = goal_range
        self._params = [0]

    def sample_env(self):
        self._params = [0]
        self._env = gym.make(self._experiment)
        self._env.env.reward_type="dense"        
    def get_env(self):
        """
            Returns a randomized environment and the vector of the parameter
            space that corresponds to this very instance
        """
        return self._env, self._params

    def get_goal(self):
        return

