import constants as c
import random

class ROBOT:
	def __init__(self, sim, wts):
		self.startingX = random.randrange(-100 * c.robotStartDistanceRange, 100 * c.robotStartDistanceRange) / 100.
		self.startingY = random.randrange(-100 * c.robotStartDistanceRange, 100 * c.robotStartDistanceRange) / 100.
		self.send_objects(sim)
		self.send_joints(sim)
		self.send_sensors(sim)
		self.send_neurons(sim)
		self.send_synapses(sim, wts)
		del self.O
		del self.J
		del self.S
		del self.SN
		del self.MN

	def send_objects(self, sim):
		self.O0 = sim.send_box(x=self.startingX, y=self.startingY, z=c.L + c.R + c.platformHeight, length=c.L, width=c.L, height=2*c.R, r=0, g=0, b=0, collision_group = "knock")
		self.O1 = sim.send_cylinder(x=self.startingX, y=c.L + self.startingY, z=c.L+c.R + c.platformHeight, length=c.L, radius=c.R, r=1, g=0, b=0, r1=0, r2=1, r3=0, collision_group = "stand")
		self.O2 = sim.send_cylinder(x=c.L + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight, length=c.L, radius=c.R, r=0, g=1, b=0, r1=1, r2=0, r3=0, collision_group = "stand")
		self.O3 = sim.send_cylinder(x=self.startingX, y=-c.L + self.startingY, z=c.L+c.R + c.platformHeight, length=c.L, radius=c.R, r=0, g=0, b=1, r1=0, r2=1, r3=0, collision_group = "stand")
		self.O4 = sim.send_cylinder(x=-c.L + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight, length=c.L, radius=c.R, r=1, g=0, b=1, r1=1, r2=0, r3=0, collision_group = "stand")
		self.O5 = sim.send_cylinder(x=self.startingX, y=c.L*3/2 + self.startingY, z=c.L/2+c.R + c.platformHeight, length=c.L, radius=c.R, r=1, g=0, b=0, r1=0, r2=0, r3=1, collision_group = "stand")
		self.O6 = sim.send_cylinder(x=c.L*3/2 + self.startingX, y=self.startingY, z=c.L/2+c.R + c.platformHeight, length=c.L, radius=c.R, r=0, g=1, b=0, r1=0, r2=0, r3=1, collision_group = "stand")
		self.O7 = sim.send_cylinder(x=self.startingX, y=-c.L*3/2 + self.startingY, z=c.L/2+c.R + c.platformHeight, length=c.L, radius=c.R, r=0, g=0, b=1, r1=0, r2=0, r3=1, collision_group = "stand")
		self.O8 = sim.send_cylinder(x=-c.L*3/2 + self.startingX, y=self.startingY, z=c.L/2+c.R + c.platformHeight, length=c.L, radius=c.R, r=1, g=0, b=1, r1=0, r2=0, r3=1, collision_group = "stand")
		#self.O9 = sim.send_cylinder(x=0, y=c.L/2, z=c.L+2*c.R, length=c.L, radius=c.R, r=1, g=0, b=0, r1=1, r2=0, r3=0)
		#self.O10 = sim.send_cylinder(x=c.L/2, y=0, z=c.L+2*c.R, length=c.L, radius=c.R, r=0, g=1, b=0, r1=0, r2=1, r3=0)
		#self.O11 = sim.send_cylinder(x=0, y=-c.L/2, z=c.L+2*c.R, length=c.L, radius=c.R, r=0, g=0, b=1, r1=1, r2=0, r3=0)
		#self.O12 = sim.send_cylinder(x=-c.L/2, y=0, z=c.L+2*c.R, length=c.L, radius=c.R, r=1, g=0, b=1, r1=0, r2=1, r3=0)
		self.O = {}
		self.O[0] = self.O0
		self.O[1] = self.O1
		self.O[2] = self.O2
		self.O[3] = self.O3
		self.O[4] = self.O4
		self.O[5] = self.O5
		self.O[6] = self.O6
		self.O[7] = self.O7
		self.O[8] = self.O8

	def send_joints(self, sim):
		self.J0 = sim.send_hinge_joint(x=self.startingX, y=c.L/2 + self.startingY, z=c.L+c.R + c.platformHeight, n1=-1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O1)
		self.J1 = sim.send_hinge_joint(x=self.startingX, y=c.L*3/2 + self.startingY, z=c.L+c.R + c.platformHeight, n1=-1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O1, second_body_id = self.O5)
		self.J2 = sim.send_hinge_joint(x=c.L/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight, n1=0, n2=1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O2)
		self.J3 = sim.send_hinge_joint(x=c.L*3/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight, n1=0, n2=1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O2, second_body_id = self.O6)
		self.J4 = sim.send_hinge_joint(x=self.startingX, y=-c.L/2 + self.startingY, z=c.L+c.R + c.platformHeight, n1=1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O3)
		self.J5 = sim.send_hinge_joint(x=self.startingX, y=-c.L*3/2 + self.startingY, z=c.L+c.R + c.platformHeight, n1=1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O3, second_body_id = self.O7)
		self.J6 = sim.send_hinge_joint(x=-c.L/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight, n1=0, n2=-1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O0, second_body_id = self.O4)
		self.J7 = sim.send_hinge_joint(x=-c.L*3/2 + self.startingX, y=self.startingY, z=c.L+c.R + c.platformHeight, n1=0, n2=-1, n3=0, lo=-3.14159/2, hi=3.14159/2, first_body_id = self.O4, second_body_id = self.O8)
		#self.J8 = sim.send_hinge_joint(x=0, y=c.L/2, z=c.L+c.R, n1=1, n2=0, n3=0, lo=0, hi=0, first_body_id = self.O0, second_body_id = self.O9)
		#self.J9 = sim.send_hinge_joint(x=c.L/2, y=0, z=c.L+c.R, n1=0, n2=1, n3=0, lo=0, hi=0, first_body_id = self.O0, second_body_id = self.O10)
		#self.J10 = sim.send_hinge_joint(x=0, y=-c.L/2, z=c.L+c.R, n1=-1, n2=0, n3=0, lo=0, hi=0, first_body_id = self.O0, second_body_id = self.O11)
		#self.J11 = sim.send_hinge_joint(x=-c.L/2, y=0, z=c.L+c.R, n1=0, n2=-1, n3=0, lo=0, hi=0, first_body_id = self.O0, second_body_id = self.O12)
		# we only add the joints we want controlled by the newtwork to this dictionary
		self.J = {}
		self.J[0] = self.J0
		self.J[1] = self.J1
		self.J[2] = self.J2
		self.J[3] = self.J3
		self.J[4] = self.J4
		self.J[5] = self.J5
		self.J[6] = self.J6
		self.J[7] = self.J7

	def send_sensors(self, sim):
		self.T0 = sim.send_touch_sensor(body_id = self.O5)
		self.T1 = sim.send_touch_sensor(body_id = self.O6)
		self.T2 = sim.send_touch_sensor(body_id = self.O7)
		self.T3 = sim.send_touch_sensor(body_id = self.O8)
		#self.L1 = sim.send_light_sensor(body_id = self.O9)
		#self.L2 = sim.send_light_sensor(body_id = self.O10)
		#self.L3 = sim.send_light_sensor(body_id = self.O11)
		#self.L4 = sim.send_light_sensor(body_id = self.O12)
		self.R0 = sim.send_ray_sensor(body_id = self.O0, x = 0, y = c.L/2, z = c.L + c.R, r1 = 0, r2 = 1, r3 = 0, max_distance=10)
		self.R1 = sim.send_ray_sensor(body_id = self.O0, x = c.L/2, y = 0, z = c.L + c.R, r1 = 1, r2 = 0, r3 = 0, max_distance=10)
		self.R2 = sim.send_ray_sensor(body_id = self.O0, x = 0, y = -c.L/2, z = c.L + c.R, r1 = 0, r2 = -1, r3 = 0, max_distance=10)
		self.R3 = sim.send_ray_sensor(body_id = self.O0, x = -c.L/2, y = 0, z = c.L + c.R, r1 = -1, r2 = 0, r3 = 0, max_distance=10)
		self.V0 = sim.send_vestibular_sensor(body_id = self.O0)
		#self.L4 = sim.send_light_sensor(body_id = self.O0)
		self.P1 = sim.send_position_sensor(body_id = self.O0)
		# we only add the sensors we wish to be part of the network to this dictionary
		self.S = {}
		self.S[0] = self.T0
		self.S[1] = self.T1
		self.S[2] = self.T2
		self.S[3] = self.T3
		self.S[4] = self.R0
		self.S[5] = self.R1
		self.S[6] = self.R2
		self.S[7] = self.R3
		self.S[8] = self.V0
		#self.S[4] = self.L1
		#self.S[5] = self.L2
		#self.S[6] = self.L3
		#self.S[7] = self.L4
		#self.S[4] = self.L4

	def send_neurons(self, sim):
		self.SN = {}
		for s in self.S:
			self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
		self.MN = {}
		for j in self.J:
			self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau = 0.5)

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
			self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau = 0.5)

	def send_synapses(self, sim, wts):
		for j in self.SN:
			for i in self.MN:
				sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts[j, i])

	def getXYPosition(self, sim):
		xPos = sim.get_sensor_data(sensor_id = self.P1, svi=0)[-1]
		yPos = sim.get_sensor_data(sensor_id = self.P1, svi=1)[-1]
		return ((xPos, yPos))
