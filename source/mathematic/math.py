import matplotlib.pyplot as plt
import math

"""https://habr.com/ru/post/146236/"""

# size = 2
# xlist = [i/3 for i in range(-1 * (size * 3), size * 3 + 1)]
# print(xlist)
# y = [(2*x**2 + 3*x +5) for x in xlist]

# y1 = [(2*x**2 + 3*x) for x in xlist]

# y2 = [(2*x**2) for x in xlist]

vector = [[1,2,4], [3,3,2], [4,1,3]]

# vector = [[12,-51,4], [6,167,-68], [-4,24,-41]]

def decomposition(a):
	return [[a[e][i] for e in range(len(a))] for i in range(len(a[0]))]
def NormOfVector(x):
	return sum([abs(i) for i in x])
def skalar_vector_composition(x, y):
	return sum([x[i]*y[i] for i in range(len(x))])	
def ScalarToVectorProduct(x, y):
	return [x*y[i] for i in range(len(y))]
def composition(x, y):
	return [x*y[i] for i in range(len(y))]
def substraction_vector(x, y):
	return [x[i] - y[i] for i in range(len(y))]
def VectorProjection(b,a):
	return composition(skalar_vector_composition(a,b)/skalar_vector_composition(b,b), b)
def qr_decomposition(a):
	av = decomposition(a)

	u = [0 for i in range(len(av))]
	e = [0 for i in range(len(av))]

	u[0] = av[0]
	e[0] = ScalarToVectorProduct(1/NormOfVector(u[0]), u[0])
	print(u[0])
	for i in range(1, len(av)):
		u[i] = av[i]
		for ei in range(i):
			print('VectorProjection',VectorProjection(u[ei], av[i]))
			u[i] = substraction_vector(u[i], VectorProjection(u[ei], av[i]))
		e[i] = composition(1/NormOfVector(u[i]), u[i])

	for i in u:
		print(i)
	print()	
	print()
	for i in e:
		print(i)
	print()	
	print()
	return [[skalar_vector_composition(av[i], e[ei]) for ei in range(len(a))] for i in range(len(a[0]))]

for i in qr_decomposition(vector):
	print(i)



exit()
plt.figure(figsize=(9, 9))
plt.subplot(3,1,1)    
plt.plot(xlist, y)
plt.title('Завиимость y = 2x^2 + 3x + 5')
plt.ylabel("y")
plt.grid(True)
plt.subplot(3,1,2)
plt.plot(xlist, y1)
plt.title("Зависимость y = 2x^2 +3x")
plt.ylabel("y1")
plt.grid(True)
plt.subplot(3,1,3)
plt.plot(xlist, y2)
plt.title("Зависимость y = 2x^2")
plt.ylabel("y2")
plt.xlabel("x")
plt.grid(True)
plt.show()
