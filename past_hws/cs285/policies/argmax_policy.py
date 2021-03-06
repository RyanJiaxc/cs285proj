import numpy as np
import pdb


class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def set_critic(self, critic):
        self.critic = critic

    def get_action(self, obs):
        # MJ: changed the dimension check to a 3
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]

        # TODO: get this from hw3

        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        q_values = self.critic.qa_values(observation)
        action = q_values.argmax(-1)
        return action[0]
    
    def get_action_personal_expl(self, obs):
        # MJ: changed the dimension check to a 3
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]

        q_values = self.critic.qa_values(observation)
        #action = q_values.argmax(-1)
        sum = np.sum(np.exp(q_values[0]))
        action = np.random.choice(q_values[0].size, p=np.exp(q_values[0])/sum)
        return action

    ####################################
    ####################################