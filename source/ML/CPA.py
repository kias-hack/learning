import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.append(os.path.abspath('../DSP'))
from correlation import cov, matrix_cov, corr, matrix_corr

def CPA(x):
	"""Метод главных компонент"""
	mean_arr = [sum([e for e in x[i]])/len(x[i]) for i in range(len(x))]
	mean_matrix = [[e - mean_arr[i] for e in x[i]] for i in range(len(x))]
	covmat = matrix_cov(mean_matrix)
	_, vecs = np.linalg.eig(covmat)
	v = [-vecs[i][1] for i in range(len(vecs))]

	return [sum([mean_matrix[e][i] * v[e] for e in range(len(mean_matrix))]) for i in range(len(mean_matrix[0]))]

x = np.arange(1,11)
y = 2 * x + np.random.randn(10) * 2

cpa = CPA([x, y])

X = [x,y]

Xcentered = (X[0] - x.mean(), X[1] - y.mean())

plt.figure(figsize=(9,9))
plt.subplot(5,1,1)
plt.title("Распределение нормированное")
plt.plot(Xcentered[0], Xcentered[1], '.')
plt.plot(range(len(cpa)),cpa, '*')
plt.grid(True)
covmat = np.cov(Xcentered)
plt.show()
exit()
Xcentered = (X[0] - x.mean(), X[1] - y.mean())
m = (x.mean(), y.mean())
print (Xcentered)
print ("Mean vector: ", m)

plt.figure(figsize=(9,9))
plt.subplot(5,1,1)
plt.title("Распределение нормированное")
plt.plot(Xcentered[0], Xcentered[1], '.')
plt.grid(True)
covmat = np.cov(Xcentered)




plt.plot([covmat[0,0], covmat[1,0]], [covmat[0,1], covmat[1,1]])

plt.show()
print(covmat)