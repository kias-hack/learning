import numpy as np
from math import sin, pi
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
from scipy import signal as scisignal

def sinus(freq, num_samples, phase = 0):
    """" Генерирует синусоиду """
    dt = 1/num_samples

    times = np.array([dt * sample for sample in range(num_samples)])

    signal = np.sin(times * 2 * pi * freq + phase)

    return times, signal

def sinus_90(freq, num_samples, phase = 0):
    """" Генерирует синусоиду сдвинутую на 90 градусов """
    dt = 1/num_samples

    times = np.array([dt * sample for sample in range(num_samples)])

    signal = np.cos(times * 2 * pi * freq + phase)

    return times, signal

NUM_SAMPLES = 10000 * 10

labels, carrier = sinus(10000, NUM_SAMPLES) # Несущая 10000 Гц
_, heterodyne_freq  = sinus(9000, NUM_SAMPLES) # I поток гетеродина 9000 Гц
_, heterodyne_freq_90  = sinus_90(9000, NUM_SAMPLES) # Q поток гетеродина 9000 Гц
_, signal = sinus(100, NUM_SAMPLES) # сигнал 100 Гц

carrier = carrier * ((signal * 0.5) + 0.5) # производим модуляцию несущую полузным сигналом

# Преобразование частот в гетеродине и получение I и Q потоков
i = carrier * heterodyne_freq
q = carrier * heterodyne_freq_90

# Объединение I и Q потоков в комплексую форму
csig = i + 1j * q
csig = 2 * csig

# Вычисление спектра несущей с полезным сигналом
y_spectrum = (2.0 / NUM_SAMPLES) * np.abs(fft(carrier)[:NUM_SAMPLES//2])
x_spectrum = fftfreq(NUM_SAMPLES, 1/NUM_SAMPLES)[:NUM_SAMPLES//2]

# Вычисление спектра сигнала на промежуточной частоте 
y_spectrum_add = (2.0 / NUM_SAMPLES) * np.abs(fft(csig))
x_spectrum_add = fftfreq(NUM_SAMPLES, 1/NUM_SAMPLES)

_, prog_heterodyne_freq  = sinus(1000, NUM_SAMPLES) # Программный гетеродин 1000 Гц

# Перенос на нулевую частоту
zero = csig * prog_heterodyne_freq

# Вычисление на нулевой частоте 
y_spectrum_prog = (2.0 / NUM_SAMPLES) * np.abs(fft(zero))
x_spectrum_prog = fftfreq(NUM_SAMPLES, 1/NUM_SAMPLES)
 
# Фильтр 500 Гц
wn3 = 2 * 500 / NUM_SAMPLES
b, a = scisignal.butter(8, wn3, "lowpass")

# Детектируем (диод)
original_signal = np.array([sample if sample > 0 else 0 for sample in csig])
original_signal = scisignal.filtfilt(b, a, original_signal)

fig, ((ax0, ax1),(ax2, ax3), (ax4, ax5)) = plt.subplots(3, 2)
ax0.plot(labels, carrier)
ax0.set_title("График несущей частоты")
ax0.set_xlabel("Время")
ax0.set_ylabel("Амплитуда")

ax1.plot(labels, csig)
ax1.set_title("График смешенного сигнала с гетеродином")
ax1.set_xlabel("Время")
ax1.set_ylabel("Амплитуда")

ax2.plot(x_spectrum, y_spectrum)
ax2.set_title("Спектр исходного модулированного сигнала")
ax2.set_xlabel("Частота")
ax2.set_ylabel("Амплитуда")

ax3.plot(x_spectrum_add, y_spectrum_add)
ax3.set_title("Спектр смешенного сигнала с гетеродином")
ax3.set_xlabel("Частота")
ax3.set_ylabel("Амплитуда")

ax4.plot(x_spectrum_prog, y_spectrum_prog)
ax4.set_title("Спектр сигнала на нулевой частоте")
ax4.set_xlabel("Частота")
ax4.set_ylabel("Амплитуда")


ax5.plot(labels, original_signal)
ax5.set_title("График сдетектированного переданного сигнала")
ax5.set_xlabel("Время")
ax5.set_ylabel("Амплитуда")

plt.show()  