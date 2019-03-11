from environments import ENVIRONMENTS
from population import POPULATION
import constants as c

envs = ENVIRONMENTS()

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=True, pb=True)


for g in range(1, c.numGens+1):
	children = POPULATION(c.popSize)
	children.Fill_From(parents)
	children.Evaluate(envs, pp=False, pb=True)
	print(g),
	children.Print()
	parents = children

bestPop = POPULATION(1)
bestPop.p[0] = parents.p[0]
bestPop.Evaluate(envs, pp=False, pb=False)
