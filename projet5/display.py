from matplotlib import pyplot as plt
import numpy as np

def display(f, min=0, max=1, sample=100):
	X = np.linspace(min, max, sample)
	Y = np.array(list(map(f,X)))
	plt.figure()
	plt.plot(X,Y)
	plt.show()
