import math
import matplotlib.pyplot as plt
import random
import numpy as np

def convolution(x,y):
	"""Свретка сигнала"""
	ylen = len(y)
	xlen = len(x)
	sumlen = ylen + xlen
	#return [sum([(x[i+yi] * y[yi])/sumlen for yi in range(ylen)]) for i in range(xlen-ylen)]
	return [corr([x[i+offset] for i in range(ylen)], y) for offset in range(xlen-ylen)]

def corr(x,y):
	"""Корреляция двух векторов - показывает на сколько зависит один вектор от другого значения -1 до 1"""
	N = len(x)
	x_mean = sum([i for i in x])/N
	y_mean = sum([i for i in y])/N
	return sum([(x[i] - x_mean)*(y[i] - y_mean) for i in range(N)])/math.sqrt(sum([math.pow(x[i] - x_mean, 2) for i in range(N)])*sum([math.pow(y[i] - y_mean, 2) for i in range(N)]))

def matrix_corr(xy):
	"""Матрица корреляции"""
	size_matrix = len(xy)
	z = [[0 for i in range(size_matrix)] for e in range(size_matrix)]
	

	for row in range(size_matrix):
		for num in range(size_matrix):
			z[row][num] = corr(xy[row], xy[num])

	return z


def cov(x,y):
	"""Ковариация"""
	x_len = len(x)
	y_len = len(y)
	x_mean = sum([i for i in x])/x_len
	y_mean = sum([i for i in y])/y_len

	return sum([(x[i]-x_mean)*(y[i] - y_mean) for i in range(x_len)])/(x_len-1)

def matrix_cov(xy):
	"""Матрица ковариаций"""
	size_matrix = len(xy)
	z = [[0 for i in range(size_matrix)] for e in range(size_matrix)]
	

	for row in range(size_matrix):
		for num in range(size_matrix):
			z[row][num] = cov(xy[row], xy[num])

	return z

size_noise_extens = 32
y = [1, 2, 4, 2, 3]
h = [2, 2, 0, 0, 2, 2]

y = [math.sin(2*math.pi*10000*i/48000) for i in range(10)]

random_signal = [random.random() for i in range(size_noise_extens)]
noise_signal = random_signal + y + random_signal
noise_signal = [random.random() + i for i in noise_signal]

# x1 = list(reversed(noise_signal))
x1 = noise_signal


z = convolution(x1,y)
x = range(len(y))

def positive(x):
	if x >= 0:
		return x
	return 0

z = [positive(i) for i in z]

# plt.figure(figsize=(9,9))
# plt.subplot(3,1,1)
# plt.plot(range(size_noise_extens,size_noise_extens+len(y)), y, marker=".", color="blue")
# plt.plot(range(len(noise_signal)), noise_signal, marker=".", color="red")

# plt.subplot(3,1,2)
# x = [i * (len(noise_signal)/(len(noise_signal)-len(y))) for i in range(len(z))]
# plt.plot(x, z, marker=".", color="green")
# plt.grid()

# plt.show()