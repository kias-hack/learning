import math
import matplotlib.pyplot as plt
import random

def convolution(x,y):
	"""Свретка сигнала"""
	return [sum([x[i+yi] * y[yi] for yi in range(len(y))]) for i in range(len(x)-len(y))]

h = [1, 2, 4, 2, 3]
y = [4, 2, 1, 2, 3]

random_signal = [random.random() for i in range(4)]

noise_signal = random_signal + y + random_signal

noise_signal = [random.random() + i for i in noise_signal]

x1 = list(reversed(noise_signal))

z = convolution(x1,y)
x = range(len(y))

plt.figure(figsize=(9,9))
plt.subplot(3,1,1)
plt.plot(range(4,9), y, marker=".", color="blue")
plt.plot(range(len(noise_signal)), noise_signal, marker=".", color="red")

plt.subplot(3,1,2)
plt.plot(range(len(z)), z, marker=".", color="green")
plt.grid()

plt.show()