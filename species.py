from individual import INDIVIDUAL
import random
import copy

class SPECIES:
	def __init__(self, speciesSize, color, eval_time, mutationRate, position):
		self.speciesSize = speciesSize
		self.p = {}
		self.color = color
		self.eval_time = eval_time
		self.mutationRate = mutationRate
		self.position = position

	def getAverageFitness(self):
		fitnesses = []
		for i in self.p:
			fitnesses.append(self.p[i].getFitness())
		average = sum(fitnesses) / len(fitnesses)
		return (average)

	def Initialize(self):
		for i in range(0, self.speciesSize):
			self.p[i] = INDIVIDUAL(i, self.color, self.eval_time, self.mutationRate, self.position)

	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()

	def ReplaceWith(self, other):
		for i in self.p:
			if (self.p[i].getFitness() < other.p[i].getFitness()):
				self.p[i] = other.p[i]

	def Fill_From(self, other, num):
		self.Copy_Best_From(other, num)
		self.Collect_Children_From(other)
		for i in self.p:
			self.p[i].ID = i
			self.p[i].color = self.color

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
		while (len(self.p) < self.speciesSize):
			winner = other.Winner_Of_Tournament_Selection(other)
			winner_copy = copy.deepcopy(winner)
			index = len(self.p)
			self.p[index] = winner_copy
			self.p[index].Mutate()

	def Winner_Of_Tournament_Selection(self, other):
		p1 = random.randint(0, other.speciesSize-1)
		p2 = p1
		while (p1 == p2):
			p2 = random.randint(0, other.speciesSize-1)
		if (other.p[p1].getFitness() > other.p[p2].getFitness()):
			return (other.p[p1])
		else:
			return (other.p[p2])

	def clearFitnessScores(self):
		for i in self.p:
			self.p[i].clearFitnessScores()

	def getIndividualList(self, number):
		toSelect = [i for i in self.p]
		toTest = []
		while (len(toTest) < number):
			selectionIndex = random.choice(toSelect)
			toSelect.remove(selectionIndex)
			toTest.append(self.p[selectionIndex])
			if (len(toSelect) == 0):
				toSelect = [i for i in self.p]
		return (toTest)

	def getMostFitMember(self):
		memberList = []
		for i in self.p:
			memberList.append(self.p[i])
		sortedMembers = sorted(memberList, reverse=True)
		for i in self.p:
			self.p[i].Print()
		return (sortedMembers[0])
