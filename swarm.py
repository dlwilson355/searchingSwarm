from species import SPECIES
import random
import constants as c
import pyrosim

class SWARM:
	def __init__(self, numSpecies, speciesSize, mutationRate, evalTime, numEnvs):
		self.species = {}
		self.numSpecies = numSpecies
		self.speciesSize = speciesSize
		self.mutationRate = mutationRate
		self.evalTime = evalTime
		self.numEnvs = numEnvs

	def Print(self):
		print("[ "),
		for i in self.species:
			print(str(i) + ": " + str(self.species[i].getAverageFitness()) + ", "),
		print("]")

	def getFitnesses(self):
		fitnesses = []
		for i in self.species:
			fitnesses.append(self.species[i].getAverageFitness())
		return (fitnesses)

	def evaluateSwarms(self, envs, pp, pb):
		# make sure all the fitness scores are cleared before evaluation
		for i in self.species:
			self.species[i].clearFitnessScores()

		swarms = self.buildSwarms()
		sims = []
		for e in range(self.numEnvs):
			sim = pyrosim.Simulator(eval_time = self.evalTime, play_paused = pp, play_blind = pb)
			for member in swarms[e]:
				member.sendRobotToSimulator(sim)
			envs.envs[e].buildEnvironment()
			envs.envs[e].sendEnvironmentToSimulator(sim)
			sim.start()
			sims.append(sim)

		for e in range(self.numEnvs):
			sim = sims[e]
			sim.wait_to_finish()
			self.updateIndividualFitnessScores(swarms[e], envs.envs[e], sim)
			del sim

	# returns the swarm with the best individual from each species
	def testEliteSwarm(self, envs):
		elites = []
		for i in range(self.numSpecies):
			elites.append(self.species[i].getMostFitMember())
		sims = []
		for e in range(len(envs.envs)):
			sim = pyrosim.Simulator(eval_time = self.evalTime, play_paused = True, play_blind = False)
			for member in elites:
				member.sendRobotToSimulator(sim)
			envs.envs[e].buildEnvironment()
			envs.envs[e].sendEnvironmentToSimulator(sim)
			sim.start()
			sims.append(sim)

		for e in range(len(envs.envs)):
			sim = sims[e]
			sim.wait_to_finish()
			self.updateIndividualFitnessScores(swarms[e], envs.envs[e], sim)
			del sim

	def updateIndividualFitnessScores(self, swarm, env, sim):
		positionalDataList = self.getPositionalDataList(swarm, env, sim)
		objectKnockedOverList = env.countRobotKnockOvers(sim, positionalDataList)
		for i in range(len(swarm)):
			swarm[i].updateFitnessScoreList(sim, objectKnockedOverList[i], positionalDataList[i])

	# gets a list of the positional data from all the robots in the swarm from the simulation
	def getPositionalDataList(self, swarm, env, sim):
		positionalData = []
		for member in swarm:
			positionalData.append(member.getPositionalData(env, sim))
		return (positionalData)

	def Initialize(self):
		for i in range(0, self.numSpecies):
			self.species[i] = SPECIES(self.speciesSize, c.speciesColors[i], self.evalTime, self.mutationRate, i)
			self.species[i].Initialize()

	def Fill_From(self, other):
		for i in range(self.numSpecies):
			self.species[i] = SPECIES(self.speciesSize, c.speciesColors[i], self.evalTime, self.mutationRate, i)
			self.species[i].Fill_From(other.species[i], c.copyBest)

	# returns a list of swarms where each swarm is a list of individuals generated from the species)
	def buildSwarms(self):
		selections = []
		for i in self.species:
			selections.append(self.species[i].getIndividualList(self.numEnvs))
		swarms = []
		for i in range(len(selections[0])):
			swarm = []
			for j in range(len(selections)):
				swarm.append(selections[j][i])
			swarms.append(swarm)
		return (swarms)
