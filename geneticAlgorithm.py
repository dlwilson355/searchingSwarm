from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle

envs = ENVIRONMENTS()

if (c.loadPickledPopulation):
	parents = pickle.load(open("save.txt", "rb"))
else:
	parents = SWARM(c.swarmSize)
	parents.Initialize()
	parents.evaluateSwarmInParallel(envs, pp=True, pb=True)


for g in range(1, c.numGens+1):
	children = SWARM(c.swarmSize)
	children.Fill_From(parents, c.copyBest)
	children.evaluateSwarmInParallel(envs, pp=False, pb=True)
	print(g),
	children.Print()
	parents = children
	pickle.dump(parents, open("save.txt", "wb"))

pickle.dump(parents, open("save.txt", "wb"))
parents.evaluateSwarm(envs, pp=False, pb=False)
