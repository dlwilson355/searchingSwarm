from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle

envs = ENVIRONMENTS()
parents = pickle.load(open("save.txt", "rb"))
parents.evaluateSwarm(envs, pp=False, pb=False)
