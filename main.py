import numpy as np
import matplotlib.pyplot as plt

# Задаем функцию
def f(x):
    return np.where((x >= 0) & (x <= 1), 1, 0)

# Задаем интервал и количество точек для графика
x = np.linspace(-1, 2, 1000)
y = f(x)

# Вычисляем преобразование Фурье
fourier_transform = np.fft.fft(y)
freq = np.fft.fftfreq(len(y), x[1]-x[0])

# Строим графики
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('Исходная функция')

plt.subplot(1, 2, 2)
plt.plot(freq, np.abs(fourier_transform))
plt.title('Преобразование Фурье')

plt.show()