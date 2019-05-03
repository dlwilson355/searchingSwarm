import constants as c
import random
import math

class FALLING_OBJECT:
	def __init__(self):
		self.x = 0
		self.y = 0
		while (math.sqrt(self.x**2 + self.y**2) < c.minWallDistance):
			self.x = random.randrange(-100 * c.objectDistanceRange, 100 * c.objectDistanceRange) / 100.
			self.y = random.randrange(-100 * c.objectDistanceRange, 100 * c.objectDistanceRange) / 100.

	def createObject(self, sim):
		self.box1 = sim.send_box(x=self.x, y=self.y, z=c.objectHeight/2, mass=1, length=c.objectLength, width=c.objectHeight, height=c.objectWidth, r1=3.14, r2=random.randrange(1, 100)/100.*3.14159, r3=0, r=0, g=0, b=0, collision_group = "topple")
		self.vestibularSensor = sim.send_vestibular_sensor(body_id=self.box1)

	def sendToSim(self, sim):
		self.createObject(sim)

	def knockedOver(self, sim):
		return (abs(sim.get_sensor_data(sensor_id = self.vestibularSensor)[-1] - 1.570796) > .1)

	def determineTimestepKnockedOver(self, sim):
		vestibularData = sim.get_sensor_data(sensor_id = self.vestibularSensor)
		for i in range(len(vestibularData)):
			if (abs(sim.get_sensor_data(sensor_id = self.vestibularSensor)[-1] - 1.570796) > .1):
				return (i)
		return (-1)

	def getCoordinates(self):
		return (self.x, self.y)

	def computeEuclideanDistanceFrom(self, coordinate):
		xDiff = self.x - coordinate[0]
		yDiff = self.y - coordinate[1]
		distance = math.sqrt(xDiff**2 + yDiff**2)
		return (distance)

	# this function returns the index of the robot that knocked it over, returns -1 if no robot knocked it over
	def getKnockedOverBy(self, sim, positionalData):
		if (not self.knockedOver(sim)):
			return (-1)
		timestep = self.determineTimestepKnockedOver(sim)
		closestIndex = 0
		closestDistance = self.computeEuclideanDistanceFrom((positionalData[0][0][timestep], positionalData[0][1][timestep]))
		for i in range(1, len(positionalData)):
			distance = self.computeEuclideanDistanceFrom((positionalData[i][0][timestep], positionalData[i][1][timestep]))
			if (distance < closestDistance):
				closestDistance = distance
				closestIndex = i
		return (closestIndex)
