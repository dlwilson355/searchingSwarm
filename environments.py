import constants as c
from environment import ENVIRONMENT

class ENVIRONMENTS:
	def __init__(self, numEnvs):
		self.envs = {}
		for e in range(0, numEnvs):
			self.envs[e] = ENVIRONMENT(e, c.numObjects)
