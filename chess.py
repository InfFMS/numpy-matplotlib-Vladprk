# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску.
# Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt

x, y = int(input())-1, 8 - int(input())

data = [[0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]
        ]
fig, ax = plt.subplots()
for i in range(8):
    traektory1 = plt.Circle((x, i), 0.2, facecolor='#3aab17')
    ax.add_patch(traektory1)
    traektory1 = plt.Circle((i, y), 0.2, facecolor='#3aab17')
    ax.add_patch(traektory1)
x0, y0 = x, y
while x0 != 0 and y0 != 0:
    x0 -= 1
    y0 -= 1
while x0 != 8 and y0 != 8:
    traektory = plt.Circle((x0, y0), 0.2, facecolor='#3aab17')
    ax.add_patch(traektory)
    x0 += 1
    y0 += 1
#1ая диагональ :0
x0, y0 = x, y
while x0 != 0 and y0 != 0:
    x0 -= 1
    y0 += 1
while x0 != 8 and y0 != 8:
    traektory = plt.Circle((x0, y0), 0.2, facecolor='#3aab17')
    ax.add_patch(traektory)
    x0 += 1
    y0 -= 1
ferz = plt.Circle((x, y), 0.3, facecolor='#215111')
ax.add_patch(ferz)
plt.xticks(range(8), labels=[f"{i}" for i in range(1, 9)])
plt.yticks(range(8), labels=[f"{9-i}" for i in range(1, 9)])

plt.imshow(data, cmap='binary')
plt.show()
