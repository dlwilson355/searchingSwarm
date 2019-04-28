import random
import pyrosim
import math
import numpy
from robot import ROBOT
import constants as c

class INDIVIDUAL:
	def __init__(self, i, color):
		# shape of genome is (sensors, motors)
		self.genome = numpy.random.random((6, 8)) * 2 - 1
		self.fitnesses = []
		self.ID = i
		self.color = color

	def Print(self):
		print("Individual "),
		print(self.ID),
		print(" "),
		print(self.fitnesses),
		print("\n")

	def sendRobotToSimulator(self, sim):
		self.robot = ROBOT(sim, self.genome, self.color)

	def Start_Evaluation(self, env, pp, pb):
		self.sim = pyrosim.Simulator(eval_time = c.evalTime, play_paused = pp,
play_blind = pb)
		self.robot = ROBOT(self.sim, self.genome)
		env.sendEnvironmentToSimulator(self.sim)
		self.sim.start()

	def updateFitnessScoreList(self, sim, wallsKnockedOver, positionalData):
		fitness = 100 * wallsKnockedOver
		x = positionalData[0][-1]
		y = positionalData[1][-1]
		distanceTraveled = math.sqrt(x**2 + y**2)
		fitness += distanceTraveled
		self.fitnesses.append(fitness)

	def clearFitnessScores(self):
		self.fitnesses = []

	def getFitness(self):
		self.fitnesses = sorted(self.fitnesses)
		divider = int(len(self.fitnesses)/4)
		fitnessesToUse = self.fitnesses[divider:-1*divider]
		# temporary test
		fitnessesToUse = self.fitnesses
		fitness = sum(fitnessesToUse) / len(fitnessesToUse)
		return (fitness)

	def getPositionalData(self, env, sim):
		xPositions = sim.get_sensor_data(sensor_id = self.robot.P1, svi=0)
		yPositions = sim.get_sensor_data(sensor_id = self.robot.P1, svi=1)
		return ((xPositions, yPositions))

	def Mutate(self):
		shape = self.genome.shape
		geneToMutate = (random.randint(0, shape[0]-1), random.randint(0, shape[1]-1))
		self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], math.fabs(self.genome[geneToMutate]))
		if (self.genome[geneToMutate] > 1):
			self.genome[geneToMutate] = 1
		elif (self.genome[geneToMutate] < -1):
			self.genome[geneToMutate] = -1

	def Print(self):
		print('['),
		print(self.ID),
		print(round(self.getFitness(), 2)),
		print('] '),

	def __lt__(self, other):
		return (self.getFitness() < other.getFitness())

	def __gt__(self, other):
		return (self.getFitness() > other.getFitness())
