from environments import ENVIRONMENTS
from population import POPULATION
import constants as c
import pickle

envs = ENVIRONMENTS()

if (c.loadPickledPopulation):
	parents = pickle.load(open("working.txt", "rb"))
else:
	parents = POPULATION(c.popSize)
	parents.Initialize()
	parents.Evaluate(envs, pp=True, pb=False)


for g in range(1, c.numGens+1):
	children = POPULATION(c.swarmSize)
	children.Fill_From(parents)
	children.evaluateSwarm(envs, pp=False, pb=False)
	print(g),
	children.Print()
	parents = children

pickle.dump(parents, open("save.txt", "wb"))
bestPop = POPULATION(1)
bestPop.p[0] = parents.p[0]
bestPop.Evaluate(envs, pp=False, pb=True)
