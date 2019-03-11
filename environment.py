import constants as c
import random
import math

class ENVIRONMENT:
	def __init__(self, id, numObjects):
		self.id = id
		self.boxes = []
		self.boxCoordinates = []
		self.vestibularSensors = []

	def buildEnvironment(self):
		self.boxCoordinates = []
		for i in range(c.numObjects):
			x = random.randrange(-100 * c.objectDistanceRange, 100 * c.objectDistanceRange) / 100.
			y = random.randrange(-100 * c.objectDistanceRange, 100 * c.objectDistanceRange) / 100.
			self.boxCoordinates.append((x, y))

	def sendEnvironmentToSimulator(self, sim):
		self.boxes = []
		self.vestibularSensors = []
		for coordinate in self.boxCoordinates:
			box1 = sim.send_box(x=coordinate[0], y=coordinate[1], z=c.objectHeight/2, length=c.objectLength, width=c.objectWidth, height=c.objectHeight, r=.5, g=.5, b=.5)
			box2 = sim.send_box(x=coordinate[0], y=coordinate[1], z=c.objectHeight/2, length=c.objectWidth, width=c.objectLength, height=c.objectHeight, r=.5, g=.5, b=.5)
			vestibularSensor = sim.send_vestibular_sensor(body_id=box1)
			self.boxes.append((box1, box2))
			self.vestibularSensors.append(vestibularSensor)

	def countKnockedOver(self, sim):
		knockedOver = 0
		for sensor in self.vestibularSensors:
			if (sim.get_sensor_data(sensor_id = sensor)[-1]):
				++knockedOver
		return (knockedOver)

	def getNearestDistance(self, coordinate):
		nearestCoordinate = self.boxCoordinates[0]
		nearestDistance = self.computeEuclideanDistance(coordinate, self.boxCoordinates[0])
		for boxCoordinate in self.boxCoordinates[1:]:
			distance = self.computeEuclideanDistance(coordinate, boxCoordinate)
			if (distance < nearestDistance):
				nearestCoordinate = boxCoordinate
				nearestDistance = distance
		return (nearestDistance)

	def computeEuclideanDistance(self, coordinate1, coordinate2):
		xDiff = coordinate1[0] - coordinate2[0]
		yDiff = coordinate1[1] - coordinate2[1]
		distance = math.sqrt(xDiff**2 + yDiff**2)
		return (distance)
