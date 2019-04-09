import constants as c
import random
import math
from fallingObject import FALLING_OBJECT

class ENVIRONMENT:
	def __init__(self, id, numObjects):
		self.id = id
		self.fallingObjects = []

	def buildEnvironment(self):
		self.fallingObjects = []
		for i in range(c.numObjects):
			self.fallingObjects.append(FALLING_OBJECT())
		
	def sendEnvironmentToSimulator(self, sim):
		for fallingObject in self.fallingObjects:
			fallingObject.sendToSim(sim)
		sim.send_box(x=0, y=0, z=c.platformHeight/2, length=c.platformLength, width=c.platformLength, height=c.platformHeight, r=1, g=1, b=1, collision_group = "ground")
		sim.assign_collision("knock", "topple")
		#sim.assign_collision("topple", "topple")
		#sim.assign_collision("stand", "ground")
		#sim.assign_collision("knock", "ground")
		#sim.assign_collision("stand", "stand")

	def countKnockedOver(self, sim):
		knockedOver = 0
		for fallingObject in self.fallingObjects:
			if (fallingObject.knockedOver(sim)):
				knockedOver += 1
		return (knockedOver)

	def getNearestDistance(self, coordinate):
		nearestCoordinate = self.fallingObjects[0]
		nearestDistance = self.computeEuclideanDistance(coordinate, self.fallingObjects[0].getCoordinates())
		for fallingObject in self.fallingObjects[1:]:
			distance = self.computeEuclideanDistance(coordinate, fallingObject.getCoordinates())
			if (distance < nearestDistance):
				nearestCoordinate = fallingObject.getCoordinates()
				nearestDistance = distance
		return (nearestDistance)

	def computeEuclideanDistance(self, coordinate1, coordinate2):
		xDiff = coordinate1[0] - coordinate2[0]
		yDiff = coordinate1[1] - coordinate2[1]
		distance = math.sqrt(xDiff**2 + yDiff**2)
		return (distance)

	# takes a list of measurement's from each robot's position sensor and counts how many fallers in the environment that robot knocked over
	# returns a list of how many follows each robot knocked over with entries in the index corresponding to that robot's index in positionalData
	def countRobotKnockOvers(self, sim, positionalData):
		knockOvers = [0 for i in positionalData]
		for fallingObject in self.fallingObjects:
			knockedOverIndex = fallingObject.getKnockedOverBy(sim, positionalData)
			if (not knockedOverIndex == -1):
				knockOvers[knockedOverIndex] += 1
		return (knockOvers)
