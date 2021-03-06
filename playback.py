from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle

envs = ENVIRONMENTS(c.numEnvs)
parents = pickle.load(open("save.txt", "rb"))
parents.evaluateSwarms(envs, pp=True, pb=False)
