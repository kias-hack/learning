import matplotlib.pyplot as plt
import math

size = 2
xlist = [i/3 for i in range(-1 * (size * 3), size * 3 + 1)]
print(xlist)
y = [(2*x**2 + 3*x +5) for x in xlist]

y1 = [(2*x**2 + 3*x) for x in xlist]

y2 = [(2*x**2) for x in xlist]

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
