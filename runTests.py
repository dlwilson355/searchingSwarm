from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle
import os

def initialize_population(numSpecies, speciesSize, mutationRate, evalTime, numEnvs):
	parents = SWARM(numSpecies, speciesSize, mutationRate, evalTime, numEnvs)
	parents.Initialize()
	envs = ENVIRONMENTS()
	parents.evaluateSwarms(envs, pp=True, pb=True)
	return (parents)

def runGA(genomeFilepath, resultsFilepath, numSpecies, speciesSize, mutationRate, evalTime, numEnvs):
	allFitnessScores = {}
	envs = ENVIRONMENTS()
	parents = initialize_population()

	for g in range(1, c.numGens+1):
		children = SWARM(numSpecies, speciesSize, mutationRate, evalTime, numEnvs)
		children.Fill_From(parents)
		children.evaluateSwarms(envs, pp=False, pb=True)
		print(g),
		children.Print()
		parents = children
		allFitnessScores[g] = parents.getFitnesses()
		pickle.dump(allFitnessScores, open(resultsFilepath + ".txt", "wb"))
		pickle.dump(parents, open(genomeFilepath + ".txt", "wb"))

def main():
	tests_to_run = []

if __name__ == "__main__":
	main()
