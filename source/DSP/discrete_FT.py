import matplotlib.pyplot as plt
import math
import numpy as np

sample_rate = 48000 #Частота дискретизации
frequency = 400 #Частотаизначального сигнала
num_period = 1 #количество периодов отображаемых на графике с изначальным сигналом
num_count_signal = round(num_period*sample_rate/frequency) #количество отсчетов сигнала
vector_base_cos = range(round(num_count_signal/2)+1) #количество базисных векторов косинуса
vector_base_sin = range(1,round(num_count_signal/2)+1) #количество базисных векторов синуса
vector_base_matrix = [list() for i in range(len(vector_base_cos) + len(vector_base_sin))]

x = range(num_count_signal)

#y = [math.sin(2*math.pi*(frequency*2/sample_rate)*i)+math.sin(2*math.pi*(frequency/sample_rate)*i) for i in x]

y = [math.sin(2*math.pi*(frequency*4/sample_rate)*i)+math.sin(2*math.pi*(frequency*2/sample_rate)*i)+math.sin(2*math.pi*(frequency/sample_rate)*i) for i in x]

#y = [math.sin(2*math.pi*(frequency/sample_rate)*i) for i in x]

plt.figure(figsize=(20,20))
plt.subplot(5,1,1)
plt.title('синус исходного сигнала')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(x, y)
plt.grid()

def A_k_FT(x):
    """Пока не понял что он делает"""
    N = len(x)
    return [1/N * sum([x[n] * math.cos(2 * math.pi * k * n / N) for n in range(N)]) for k in range(int(N/2))]
def B_k_FT(x):
    """Возвращает спектр сигнала - Прямое преобразование фурье"""
    N = len(x)
    return [2/N * sum([x[n] * math.sin(2 * math.pi * k * n / N) for n in range(N)]) for k in range(int(N/2))]

def reverseFT(Xk):
	"""Обратное преобразование Фурье"""
	N = len(Xk) * 2

	return [sum([Xk[f]*math.sin(f*n*2*math.pi/N) for f in range(len(Xk))]) for n in range(N)]

def quad(type_sig, num_point):
	"""Генерация ряда фурье для квадрата при остатке от деления на > 0 и для треугольника при остатке от деления равном 0"""
	for i in range(num_point):
		if i == 0:
			yield  0
		elif (i % 2 > 0 and type_sig == "quad"):
			yield 1/i
		elif (i % 2  == 0 and type_sig == "triangle"):
			yield 1/i
		else:
			yield 0

y_ft = B_k_FT(y) #Ряд фурье для исходного сигнала в начале файла по самописной функции

plt.subplot(5,1,2)
plt.title('Преобразование фурье курильщика')
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.plot([i * (sample_rate/num_count_signal) for i in range(int(len(x)/2))], y_ft)    
#[i * (sample_rate/num_count_signal) for i in range(int(len(x)/2))]   алгоритм преобразования отсчетов ДПФ в спектр сигнала
plt.grid()

fft_y = np.fft.rfft(y) #прямое преобразование фурье из библиотеки numpy 

plt.subplot(5,1,3)
plt.title('Преобразование фурье здорового человека')
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.plot(np.fft.rfftfreq(num_count_signal, 1./sample_rate), [abs(i)/num_count_signal for i in fft_y], 'bo')
plt.grid()

square_ft = list(quad("triangle", 50)) #построение ряда фурье triangle или quad

a = reverseFT(square_ft) #построение сигнала по ряду фурье для функции quad

plt.subplot(5,1,4)
plt.plot(range(len(a)), a)
plt.title("Постороение сигнала по ряду Фурье")
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.grid()

plt.subplot(5,1,5)
plt.plot(range(len(square_ft)), square_ft, 'bo')
plt.title("Ряд фурье по которому строился сигнал")
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.grid()

plt.show()
