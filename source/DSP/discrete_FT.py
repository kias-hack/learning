import matplotlib.pyplot as plt
import math
import numpy as np

sample_rate = 8000 #Частота дискретизации
frequency = 400 #Частотаизначального сигнала
num_period = 2 #количество периодов отображаемых на графике с изначальным сигналом
num_count_signal = round(num_period*sample_rate/frequency) #количество отсчетов сигнала
vector_base_cos = range(round(num_count_signal/2)+1) #количество базисных векторов косинуса
vector_base_sin = range(1,round(num_count_signal/2)+1) #количество базисных векторов синуса
vector_base_matrix = [list() for i in range(len(vector_base_cos) + len(vector_base_sin))]

x = range(num_count_signal)

y = [math.sin(2*math.pi*(frequency*2/sample_rate)*i)+math.sin(2*math.pi*(frequency/sample_rate)*i) for i in x]

#y = [math.sin(2*math.pi*(frequency/sample_rate)*i) for i in x]

plt.figure(figsize=(9,9))
plt.subplot(3,1,1)
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
    """Возвращает спектр сигнала"""
    N = len(x)
    return [2/N * sum([x[n] * math.sin(2 * math.pi * k * n / N) for n in range(N)]) for k in range(int(N/2))]

def discrete_ft(x):
    """Возможно это обратное преобразование Фурье"""
    N = len(x)
    def A(x, n, N, k):
        return 1/N * sum([x[n] * math.cos(2 * math.pi * k * n / N) for n in range(N)])
    def B(x, n, N, k):
        return 2/N * sum([x[n] * math.sin(2 * math.pi * k * n / N) for n in range(N)])
    return [sum([B(x, n, N, k) * math.sin(2 * math.pi * k * n / N) + A(x, n, N, k) * math.cos(2 * math.pi * k * n / N) for k in range(int(N/2))]) for n in range(N)]

y_ft = B_k_FT(y)

plt.subplot(3,1,2)
plt.title('Преобразование фурье курильщика')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot([i * (sample_rate/num_count_signal) for i in range(int(len(x)/2))], y_ft)    #[i * (sample_rate/num_count_signal) for i in range(int(len(x)/2))]   алгоритм преобразования ответов ДПФ в спектр сигнала
plt.grid()

fft_y = np.fft.rfft(y)

plt.subplot(3,1,3)
plt.title('Преобразование фурье здорового человека')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(np.fft.rfftfreq(num_count_signal, 1./sample_rate), [abs(i)/num_count_signal for i in fft_y])
plt.grid()

plt.show()
