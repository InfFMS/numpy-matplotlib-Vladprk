# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графикa.
from random import randint as ran
import matplotlib.pyplot as plt

categories = [i for i in range(-25, 36)]
values = [0 for i in range(-25, 36)]
data = []
l_max = -1
l_exp = 0
summ = 0
k_max_t = 0
for i in range(365):
    a = ran(-25, 35)
    values[a+25] += 1
    if a > 25:
        k_max_t += 1
    if a < 0:
        l_exp += 1
    else:
        if l_exp >= l_max:
            l_max = l_exp
            l_exp = 0
    data.append(a)
    summ += a
sr_t = round(summ/365, 2)
print(sr_t)
print(k_max_t)
print(l_max)

x = [i for i in range(1, 366)]
fig1, ax1 = plt.subplots(1, 2)
ax1[0].plot(x, data)
plt.xlabel('Дни')
plt.ylabel('Температура')
for i in range(365):
    if data[i] <= 0:
        tochka = plt.Circle((i + 1, data[i]), 1, facecolor='blue')
        ax1[0].add_patch(tochka)
    else:
        tochka = plt.Circle((i + 1, data[i]), 1, facecolor='red')
        ax1[0].add_patch(tochka)

im = ax1[1].bar(categories, values, color='#215111')

plt.show()

