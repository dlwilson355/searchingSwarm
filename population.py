from individual import INDIVIDUAL
import copy
import random
import constants as c

class POPULATION:
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

	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()

	def ReplaceWith(self, other):
		for i in self.p:
			if (self.p[i].fitness < other.p[i].fitness):
				self.p[i] = other.p[i]

	def Initialize(self):
		for i in range(0, self.popSize):
			self.p[i] = INDIVIDUAL(i)

	def Fill_From(self, other):
		self.Copy_Best_From(other)
		self.Collect_Children_From(other)

	def Copy_Best_From(self, other):
		fittest_individual = other.p[0]
		for i in other.p:
			if (other.p[i].fitness > fittest_individual.fitness):
				fittest_individual = other.p[i]
		fittest_individual_copy = copy.deepcopy(fittest_individual)
		self.p[0] = fittest_individual_copy

	def Collect_Children_From(self, other):
		for i in range(1, self.popSize):
			winner = other.Winner_Of_Tournament_Selection()
			winner_copy = copy.deepcopy(winner)
			self.p[i] = winner_copy
			self.p[i].Mutate()

	def Winner_Of_Tournament_Selection(other):
		p1 = random.randint(0, other.popSize-1)
		p2 = p1
		while (p1 == p2):
			p2 = random.randint(0, other.popSize-1)
		if (other.p[p1].fitness > other.p[p2].fitness):
			return (other.p[p1])
		else:
			return (other.p[p2])
