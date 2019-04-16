from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle
import os

def initialize_population():
	parents = SWARM(c.swarmSize)
	parents.Initialize()
	parents.evaluateSwarmInParallel(envs, pp=True, pb=True)
	return (parents)

def main():
	envs = ENVIRONMENTS()
	if (c.loadPickledPopulation):
		if (os.path.isfile("save.txt")):
			parents = pickle.load(open("save.txt", "rb"))
		else:
			parents = initialize_population()
	else:
		parents = initialize_population()

	for g in range(1, c.numGens+1):
		children = SWARM(c.swarmSize)
		children.Fill_From(parents, c.copyBest)
		children.evaluateSwarmInParallel(envs, pp=False, pb=True)
		print(g),
		children.Print()
		parents = children
		pickle.dump(parents, open("save.txt", "wb"))

if __name__ == "__main__":
	main()
