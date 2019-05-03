from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle
import os

def initialize_population():
	parents = SWARM(c.numSpecies, c.speciesSize, c.mutationRate, c.evalTime, c.numEnvs)
	parents.Initialize()
	envs = ENVIRONMENTS(c.numEnvs)
	parents.evaluateSwarms(envs, pp=True, pb=True)
	return (parents)

def main():
	envs = ENVIRONMENTS(c.numEnvs)
	if (c.loadPickledPopulation and os.path.isfile("save.txt")):
		parents = pickle.load(open("save.txt", "rb"))
	else:
		parents = initialize_population()

	for g in range(1, c.numGens+1):
		children = SWARM(c.numSpecies, c.speciesSize, c.mutationRate, c.evalTime, c.numEnvs)
		children.Fill_From(parents)
		children.evaluateSwarms(envs, pp=False, pb=True)
		print(g),
		children.Print()
		parents = children
		pickle.dump(parents, open("save.txt", "wb"))

if __name__ == "__main__":
	main()
