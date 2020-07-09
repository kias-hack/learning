import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11)
y = 2 * x + np.random.randn(10)*2
X = np.vstack((x,y))
print (X)

Xcentered = (X[0] - x.mean(), X[1] - y.mean())
m = (x.mean(), y.mean())
print (Xcentered)
print ("Mean vector: ", m)

plt.figure(figsize=(9,9))
plt.subplot(5,1,1)
plt.title("Распределение нормированное")
plt.plot(Xcentered[0], Xcentered[1])
plt.grid(True)
covmat = np.cov(Xcentered)
plt.plot([covmat[0,0], covmat[1,0]], [covmat[1,1], covmat[1,1]])

plt.show()
print(covmat)