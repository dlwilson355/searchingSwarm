from individual import INDIVIDUAL
import copy
import random
import constants as c
import pyrosim

class SWARM:
	def __init__(self, popSize):
		self.p = {}
		self.popSize = popSize

	def Print(self):
		for i in self.p:
			self.p[i].Print()
		print("")

	def Evaluate(self, envs, pp, pb):
		for i in self.p:
			self.p[i].fitness = 0.0
		for e in range(c.numEnvs):
			envs.envs[e].buildEnvironment()
			for i in self.p:
				self.p[i].Start_Evaluation(envs.envs[e], pp, pb)
			for i in self.p:
				self.p[i].Compute_Fitness(envs.envs[e])
		for i in self.p:
			self.p[i].fitness /= c.numEnvs

	def evaluateSwarm(self, envs, pp, pb):
		for i in self.p:
			self.p[i].fitness = 0.0
		for e in range(c.numEnvs):
			sim = pyrosim.Simulator(eval_time = c.evalTime, play_paused = pp,
	play_blind = pb)
			for i in self.p:
				self.p[i].sendRobotToSimulator(sim)
			envs.envs[e].buildEnvironment()
			envs.envs[e].sendEnvironmentToSimulator(sim)
			sim.start()
			sim.wait_to_finish()
			self.updateRobotFitnessValues(envs.envs[e], sim)
			del sim

	def evaluateSwarmInParallel(self, envs, pp, pb):
		for i in self.p:
			self.p[i].clearFitnessScores()
		sims = []
		for e in range(c.numEnvs):
			sim = pyrosim.Simulator(eval_time = c.evalTime, play_paused = pp,
	play_blind = pb)
			for i in self.p:
				self.p[i].sendRobotToSimulator(sim)
			envs.envs[e].buildEnvironment()
			envs.envs[e].sendEnvironmentToSimulator(sim)
			sim.start()
			sims.append(sim)

		for e in range(c.numEnvs):
			sim = sims[e]
			sim.wait_to_finish()
			self.updateRobotFitnessValues(envs.envs[e], sim)
			del sim

	def updateRobotFitnessValues(self, env, sim):
		positionalData = self.getPositionalData(env, sim)
		numberObjectsKnockedOver = env.countRobotKnockOvers(sim, positionalData)
		#print("knocked over")
		#print(numberObjectsKnockedOver)
		for i in range(len(numberObjectsKnockedOver)):
			self.p[i].updateFitness(sim, numberObjectsKnockedOver[i], positionalData[i])

	def getPositionalData(self, env, sim):
		positionalData = []
		for i in self.p:
			positionalData.append(self.p[i].getPositionalData(env, sim))
		return (positionalData)

	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()

	def ReplaceWith(self, other):
		for i in self.p:
			if (self.p[i].getFitness() < other.p[i].getFitness()):
				self.p[i] = other.p[i]

	def Initialize(self):
		for i in range(0, self.popSize):
			self.p[i] = INDIVIDUAL(i)

	def Fill_From(self, other):
		self.Copy_Best_From(other)
		self.Collect_Children_From(other)

	def Fill_From(self, other, num):
		self.Copy_Best_From(other, num)
		self.Collect_Children_From(other)

	def Copy_Best_From(self, other):
		fittest_individual = other.p[0]
		for i in other.p:
			if (other.p[i].getFitness() > fittest_individual.getFitness()):
				fittest_individual = other.p[i]
		fittest_individual_copy = copy.deepcopy(fittest_individual)
		self.p[0] = fittest_individual_copy

	def Copy_Best_From(self, other, num):
		otherPopList = []
		for i in other.p:
			otherPopList.append(other.p[i])
		otherPopList = sorted(otherPopList, reverse=True)
		i = 0
		while (i < num):
			self.p[i] = otherPopList[i]
			i += 1

	def Collect_Children_From(self, other):
		while (len(self.p) < c.swarmSize):
			winner = other.Winner_Of_Tournament_Selection()
			winner_copy = copy.deepcopy(winner)
			index = len(self.p)
			self.p[index] = winner_copy
			self.p[index].Mutate()

	def Winner_Of_Tournament_Selection(other):
		p1 = random.randint(0, other.popSize-1)
		p2 = p1
		while (p1 == p2):
			p2 = random.randint(0, other.popSize-1)
		if (other.p[p1].getFitness() > other.p[p2].getFitness()):
			return (other.p[p1])
		else:
			return (other.p[p2])
