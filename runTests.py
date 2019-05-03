from environments import ENVIRONMENTS
from swarm import SWARM
import constants as c
import pickle
import os

def initialize_population(numSpecies, speciesSize, mutationRate, evalTime, numEnvs):
	parents = SWARM(numSpecies, speciesSize, mutationRate, evalTime, numEnvs)
	parents.Initialize()
	envs = ENVIRONMENTS(numEnvs)
	parents.evaluateSwarms(envs, pp=True, pb=True)
	return (parents)

def runGA(genomeFilepath, resultsFilepath, numSpecies, speciesSize, mutationRate, evalTime, numEnvs, numGens):
	allFitnessScores = {}
	envs = ENVIRONMENTS(numEnvs)
	parents = initialize_population(numSpecies, speciesSize, mutationRate, evalTime, numEnvs)

	for g in range(1, numGens+1):
		children = SWARM(numSpecies, speciesSize, mutationRate, evalTime, numEnvs)
		children.Fill_From(parents)
		children.evaluateSwarms(envs, pp=False, pb=True)
		print(g),
		children.Print()
		parents = children
		allFitnessScores[g] = parents.getFitnesses()
		pickle.dump(allFitnessScores, open(os.path.join("results", resultsFilepath + ".txt"), "wb"))
		pickle.dump(parents, open(os.path.join("results", genomeFilepath + ".txt"), "wb"))

def main():
	tests_to_run = [{"genomeFilepath": "standardGenome", "resultsFilepath": "standardResults", "numSpecies": 4, "speciesSize": 10, "mutationRate": 2, "evalTime": 2500, "numEnvs": 20, "numGens": 3}, 
			{"genomeFilepath": "1MutationGenome", "resultsFilepath": "1MutationResults", "numSpecies": 4, "speciesSize": 10, "mutationRate": 1, "evalTime": 2500, "numEnvs": 20, "numGens": 3},
			{"genomeFilepath": "200EnvsGenome", "resultsFilepath": "200EnvsResults", "numSpecies": 4, "speciesSize": 10, "mutationRate": 2, "evalTime": 2500, "numEnvs": 200, "numGens": 3},
			{"genomeFilepath": "2Species20Pop40EnvsGenome", "resultsFilepath": "2Species20Pop40EnvsResults", "numSpecies": 2, "speciesSize": 20, "mutationRate": 2, "evalTime": 2500, "numEnvs": 40, "numGens": 3}]

	for test in tests_to_run:
		print("Running test %s." % (test))
		runGA(test["genomeFilepath"], test["resultsFilepath"], test["numSpecies"], test["speciesSize"], test["mutationRate"], test["evalTime"], test["numEnvs"], test["numGens"])

if __name__ == "__main__":
	main()
