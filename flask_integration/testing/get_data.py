import numpy as np 
from matplotlib import pyplot as plt
def get_random_data():
	N = 1000
	multiplier = 10
	means = np.tile(np.arange(N//multiplier).reshape(1,N//multiplier),(1,multiplier)).flatten('F')

	data = np.random.normal(means, 5,[2,N])
	return data[0][:], data[1][:]

if __name__ == "__main__":
	a,b =get_random_data()
	plt.scatter(a, b,s=10)
	plt.show()