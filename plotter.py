import matplotlib.pyplot as plt
import glob
import os
import pickle

directory = "graph"

filepaths = glob.glob(os.path.join(directory, "*.txt"))
print(filepaths)

for filepath in filepaths:
	if ("Results" in filepath):
		data = pickle.load(open(filepath, "rb"))
		x = [sum(data[i]) for i in data]
		if ("5" in filepath):
			label = "Population Size: 5"
		elif ("10" in filepath):
			label = "Population Size: 10"
		elif ("20" in filepath):
			label = "Population Size: 20"
		else:
			label = "ERROR: Label not found"
		plt.plot(x, label=label)

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Total Fitness of Swarms at Different Population Sizes over 500 Generations")
plt.legend()
plt.show()
