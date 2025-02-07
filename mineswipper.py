# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
from random import randint as ran
import matplotlib.pyplot as plt

data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n = 15
for _ in range(n):
    i, j = ran(0, 9), ran(0, 9)
    if data[i][j] != 1:
        data[i][j] = 1
    else:
        n += 1

plt.imshow(data, cmap='Reds')

for i in range(10):
    for j in range(10):
        if data[i][j] == 1:
            data[i][j] = -1
for i in range(10):
    for j in range(10):
        if data[i][j] == -1:
            try:
                if data[i+1][j] != -1:
                    data[i+1][j] += 1
            except:
                pass
            try:
                if data[i][j+1] != -1:
                    data[i][j+1] += 1
            except:
                pass
            try:
                if data[i-1][j] != -1:
                    data[i-1][j] += 1
            except:
                pass
            try:
                if data[i][j-1] != -1:
                    data[i][j-1] += 1
            except:
                pass
            try:
                if data[i+1][j+1] != -1:
                    data[i+1][j+1] += 1
            except:
                pass
            try:
                if data[i-1][j-1] != -1:
                    data[i-1][j-1] += 1
            except:
                pass
            try:
                if data[i+1][j-1] != -1:
                    data[i+1][j-1] += 1
            except:
                pass
            try:
                if data[i-1][j+1] != -1:
                    data[i-1][j+1] += 1
            except:
                pass

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='gist_rainbow')
for i in range(10):
    for j in range(10):
        text = ax.text(j, i, data[i][j], ha="center", va="center", color="w")
plt.show()
