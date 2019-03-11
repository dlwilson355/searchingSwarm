import random
import pyrosim
import math
import numpy
from robot import ROBOT
import constants as c

class INDIVIDUAL:
	def __init__(self, i):
		# shape of genome is (sensors, motors)
		self.genome = numpy.random.random((9, 8)) * 2 - 1
		self.fitness = 0
		self.ID = i

	def Start_Evaluation(self, env, pp, pb):
		self.sim = pyrosim.Simulator(eval_time = c.evalTime, play_paused = pp,
play_blind = pb)
		self.robot = ROBOT(self.sim, self.genome)
		env.buildEnvironment(self.sim)
		self.sim.start()

	def Compute_Fitness(self, env):
		self.sim.wait_to_finish()
		#env.countKnockedOver(self.sim)
		position = self.robot.getXYPosition(self.sim)
		self.fitness -= env.getNearestDistance(position)
		#self.fitness += math.sqrt((0-self.sim.get_sensor_data(sensor_id = self.robot.P1, svi=0)[-1])**2 + (0-self.sim.get_sensor_data(sensor_id = self.robot.P1, svi=1)[-1])**2)
		#self.fitness += self.sim.get_sensor_data(sensor_id = self.robot.L1)[-1] + self.sim.get_sensor_data(sensor_id = self.robot.L2)[-1] + self.sim.get_sensor_data(sensor_id = self.robot.L3)[-1] + self.sim.get_sensor_data(sensor_id = self.robot.L4)[-1]
		del self.sim

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
		print(self.fitness),
		print('] '),
