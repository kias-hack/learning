import math
import matplotlib.pyplot as plt
from random import random 


frequency = 1000
sampling = 48000
amplitude = 5

x = range(round(10 * sampling/frequency) + 1)

y = [amplitude * math.sin(2*math.pi*frequency/sampling*i) for i in x]

y1 = [(amplitude/3) * math.sin((2*math.pi*frequency*4)/sampling*i) for i in x]

y2 = [(amplitude/4) * math.sin((2*math.pi*frequency*2)/sampling*i) for i in x]

y3 = [(amplitude/2) * random() for i in x]

y12 = [y[i] + y1[i] + y2[i] + y3[i] for i in x]

print(len(y), len(y12))

prev_value = y[0]
start = False
period = False
minAmplitude = y[0]
maxAmplitude = y[0]
signal_sum = 0
zero = 0
for i in range(1, len(y)):
    if prev_value >= zero and y[i] < zero and period is False:
        if start is False:
            start = i
            signal_sum = y[i]
        else:
            period = i - start
            print("Средняя точка находится в значении - " + str(signal_sum / period))
            start = False
    if start > 0:
        signal_sum  = signal_sum + y[i]
    if prev_value <= zero and y[i] > zero and period is False:
        if start > 0:
            print("Действующее значение сигнала - " + str(abs(signal_sum/(i - start))))
    if y[i] < minAmplitude:
        minAmplitude = y[i]
    if y[i] > maxAmplitude:
        maxAmplitude = y[i]
    prev_value = y[i]
print("Период равен ", period)
print("Частота равна ", sampling/period)
print("Размах амплитуды равен ", abs(minAmplitude) + abs(maxAmplitude))
            
plt.figure(figsize = (9,9))        
plt.subplot(2,1,1)
plt.plot(x, y)
plt.title('sinus')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x, y12)
plt.title('sinussumm')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
