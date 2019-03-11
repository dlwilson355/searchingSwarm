import constants as c
import random
import math

class ENVIRONMENT:
	def __init__(self, id, numObjects):
		self.id = id
		self.boxes = []
		self.boxCoordinates = []
		self.vestibularSensors = []

	def buildEnvironment(self, sim):
		for i in range(c.numObjects):
			x = random.randrange(-c.objectDistanceRange, c.objectDistanceRange)
			y = random.randrange(-c.objectDistanceRange, c.objectDistanceRange)
			box = sim.send_box(x=x, y=y, z=c.objectHeight/2, length=c.objectWidth, width=c.objectWidth, height=c.objectHeight, r=.5, g=.5, b=.5)
			vestibularSensor = sim.send_vestibular_sensor(body_id=box)
			self.boxes.append(box)
			self.boxCoordinates.append((x, y))
			print("coordinates")
			print(self.boxCoordinates)
			self.vestibularSensors.append(vestibularSensor)
			#lightSource = sim.send_box(x=2, y=2, z=c.objectSize/2, length=c.objectSize, width=c.objectSize, height=c.objectSize, r=.5, g=.5, b=.5)
			#sim.send_light_source(body_id=lightSource)
			#self.lightSources.append(lightSource)

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
		print("nearest coordinate")
		print(nearestCoordinate)
		return (nearestDistance)

	def computeEuclideanDistance(self, coordinate1, coordinate2):
		xDiff = coordinate1[0] - coordinate2[0]
		yDiff = coordinate1[1] - coordinate2[1]
		distance = math.sqrt(xDiff**2 + yDiff**2)
		return (distance)
