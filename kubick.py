# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
from random import randint as ran
import matplotlib.pyplot as plt


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 4, round(y[i]/1000, 3), ha='center', va='center')


chisla = ['1', '2', '3', '4', '5', '6', 'maximum']
data = [0, 0, 0, 0, 0, 0, 0]

for i in range(1000):
    x = ran(1, 6)
    data[x-1] += 1
data[6] = max(data[1], data[2], data[3], data[4], data[5])

plt.bar(chisla, data, color='#215111')
addlabels(chisla, data)
plt.title('1000 раз бросили кубик...')
plt.show()


