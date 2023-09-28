import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions.categorical import Categorical
from torch.optim import Adam
import numpy as np


def mlp(sizes, activation=nn.Tanh, output_activation=nn.Identity):
    # Build a feedforward neural network for the policy
    layers = []
    for j in range(len(sizes)-1):
        act = activation if j < len(sizes)-2 else output_activation
        layers += [nn.Linear(sizes[j], sizes[j+1]), act()]
    return nn.Sequential(*layers)


class Net(nn.Module):
    ##TODO you can code this up using whatever methods you want, 
    # but to work with the rest of the code make sure you
    # at least implement the predict_reward function below

    def __init__(self):
        super().__init__()
        #TODO define network architecture. 
        # Hint, states in cartpole are 4-dimensional (x,xdot,theta,thetadot)
        # https://www.gymlibrary.dev/environments/classic_control/cart_pole/

   

    def predict_reward(self, traj):
        '''calculate cumulative return of trajectory, could be a trajectory with a single element'''
        #TODO should take in a trajectory and output a scalar cumulative reward estimate

   