# robot constants
robotStartDistanceRange = 0.7
robotZShift = 0
L = .1
R = L/5
topMass = .1
speciesColors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
tau = 0.2

# environmental object constants
numObjects = 40
objectDistanceRange = 4
minWallDistance = 1
objectWidth = 0.01
objectLength = 0.7
objectHeight = 0.3
standBase = 0.03
platformLength = 20
platformHeight = .015

# genetic algorithm settings
loadPickledPopulation = True
speciesSize = 10
numSpecies = 4
copyBest = 3
numGens = 3000
numEnvs = 20
evalTime = 2500
mutationRate = 2
