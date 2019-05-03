import constants as c
import random

class ROBOT:
	def __init__(self, sim, wts, color):
		self.color = color
		self.startingX = random.randrange(-100 * c.robotStartDistanceRange, 100 * c.robotStartDistanceRange) / 100.
		self.startingY = random.randrange(-100 * c.robotStartDistanceRange, 100 * c.robotStartDistanceRange) / 100.
		self.send_objects(sim)
		self.send_joints(sim)
		self.send_sensors(sim)
		self.send_neurons(sim)
		self.send_synapses(sim, wts)
		del self.J
		del self.S
		del self.SN
		del self.MN

	def send_objects(self, sim):
		self.O0 = sim.send_box(x=self.startingX, y=self.startingY, z=c.L + c.R + c.platformHeight + c.robotZShift, mass = c.topMass, length=c.L, width=c.L, height=2*c.R, r=self.color[0], g=self.color[1], b=self.color[2], collision_group = "knock")
		self.O1 = sim.send_cylinder(x=self.startingX, y=c.L + self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=0, r2=1, r3=0, collision_group = "stand")
		self.O2 = sim.send_cylinder(x=c.L + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=1, r2=0, r3=0, collision_group = "stand")
		self.O3 = sim.send_cylinder(x=self.startingX, y=-c.L + self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=0, r2=1, r3=0, collision_group = "stand")
		self.O4 = sim.send_cylinder(x=-c.L + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=1, r2=0, r3=0, collision_group = "stand")
		self.O5 = sim.send_cylinder(x=self.startingX, y=c.L*3/2 + self.startingY, z=c.L/2+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=0, r2=0, r3=1, collision_group = "stand")
		self.O6 = sim.send_cylinder(x=c.L*3/2 + self.startingX, y=self.startingY, z=c.L/2+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=0, r2=0, r3=1, collision_group = "stand")
		self.O7 = sim.send_cylinder(x=self.startingX, y=-c.L*3/2 + self.startingY, z=c.L/2+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=0, r2=0, r3=1, collision_group = "stand")
		self.O8 = sim.send_cylinder(x=-c.L*3/2 + self.startingX, y=self.startingY, z=c.L/2+c.R + c.platformHeight + c.robotZShift, length=c.L, radius=c.R, r=self.color[0], g=self.color[1], b=self.color[2], r1=0, r2=0, r3=1, collision_group = "stand")
		self.O9 = sim.send_box(x=self.startingX, y=self.startingY, z=c.L + c.R + c.platformHeight + c.robotZShift + 2*c.R, mass = c.topMass, length=c.L/4, width=c.L/4, height=2*c.R, r=1, g=1, b=1, collision_group = "knock")

	def send_joints(self, sim):
		self.J0 = sim.send_hinge_joint(x=self.startingX, y=c.L/2 + self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=-1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O1)
		self.J1 = sim.send_hinge_joint(x=self.startingX, y=c.L*3/2 + self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=-1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O1, second_body_id = self.O5)
		self.J2 = sim.send_hinge_joint(x=c.L/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=0, n2=1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O2)
		self.J3 = sim.send_hinge_joint(x=c.L*3/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=0, n2=1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O2, second_body_id = self.O6)
		self.J4 = sim.send_hinge_joint(x=self.startingX, y=-c.L/2 + self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O3)
		self.J5 = sim.send_hinge_joint(x=self.startingX, y=-c.L*3/2 + self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O3, second_body_id = self.O7)
		self.J6 = sim.send_hinge_joint(x=-c.L/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=0, n2=-1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O4)
		self.J7 = sim.send_hinge_joint(x=-c.L*3/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight + c.robotZShift, n1=0, n2=-1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O4, second_body_id = self.O8)
		self.J8 = sim.send_hinge_joint(x=self.startingX, y=self.startingY, z=c.L + c.R + c.platformHeight + c.robotZShift + c.R, n1=0, n2=0, n3=1, lo=-3.14159, hi=3.14159, first_body_id = self.O0, second_body_id = self.O9)
		self.J = {}
		self.J[0] = self.J0
		self.J[1] = self.J1
		self.J[2] = self.J2
		self.J[3] = self.J3
		self.J[4] = self.J4
		self.J[5] = self.J5
		self.J[6] = self.J6
		self.J[7] = self.J7
		self.J[8] = self.J8

	def send_sensors(self, sim):
		self.T0 = sim.send_touch_sensor(body_id = self.O5)
		self.T1 = sim.send_touch_sensor(body_id = self.O6)
		self.T2 = sim.send_touch_sensor(body_id = self.O7)
		self.T3 = sim.send_touch_sensor(body_id = self.O8)
		self.R0 = sim.send_ray_sensor(body_id = self.O9, x = self.startingX, y = self.startingY, z = c.L + c.R + c.platformHeight + c.robotZShift + 3*c.R, r1 = 1, r2 = 0, r3 = 0, max_distance=2)
		self.V0 = sim.send_vestibular_sensor(body_id = self.O0)
		self.P1 = sim.send_position_sensor(body_id = self.O0)
		self.S = {}
		self.S[0] = self.T0
		self.S[1] = self.T1
		self.S[2] = self.T2
		self.S[3] = self.T3
		self.S[4] = self.R0

	def send_neurons(self, sim):
		self.SN = {}
		for s in self.S:
			self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
		for j in range(4):
			s += 1
			self.SN[s] = sim.send_sensor_neuron(sensor_id = self.V0, svi=j)
		self.MN = {}
		for j in self.J:
			self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau = 0.3)

	# creates a more complex network
	def sendNeuronsComplex(self, sim):
		self.SN = {}
		for s in self.S:
			self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
		self.HN = {}
		for i in range(len(self.SN) + len(self.MN)):
			self.HN[i] = sim.send_hidden_neuron()
		self.MN = {}
		for j in self.J:
			self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau = 0.3)
			#self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j])

	def send_synapses(self, sim, wts):
		for j in self.SN:
			for i in self.MN:
				sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts[j, i])

	def getXYPosition(self, sim):
		xPos = sim.get_sensor_data(sensor_id = self.P1, svi=0)[-1]
		yPos = sim.get_sensor_data(sensor_id = self.P1, svi=1)[-1]
		return ((xPos, yPos))
