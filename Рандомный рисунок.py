import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 9))
ax0 = fig.add_subplot()
#  X = np.arange(7)
X = np.array([0, 1, 2, 3, 4, 5, 6])

#  Y = np.arange(7)
Y = np.array([0, 1, 2, 3, 4, 5, 6])
"Характеристики для зелено-синего векторного поля"
max_u1=1500
min_u1=-1400

max_v1=400
min_v1=-600
"Характеристики для красного векторного поля"
max_u2=1500
min_u2=-1400

max_v2=400
min_v2=-600
fig, axes = plt.subplots()
u1=(max_u1-min_u1)*np.random.random((7,7))+min_u1
v1=(max_v1-min_v1)*np.random.random((7,7))+min_v1
u2=(max_u2-min_u2)*np.random.random((7,7))+min_u2
v2=(max_v2-min_v2)*np.random.random((7,7))+min_v2
"""X, Y - матрицы для задания пространства, где будут векторы, U, V - векторные поля
density-частота линий, maxlength - максимальная длина одной линии, linewidth - толщина"""
axes.streamplot(X, Y, u1,v1, color=u1+v1,density=2,maxlength=0.4,linewidth=2-u1/v1,arrowstyle = "->")
axes.streamplot(X, Y, u2,v2, color="crimson",density=1.5)

fig.set_figwidth(8)    #  ширина и
fig.set_figheight(8)    #  высота "Figure"
plt.grid(b=False)
plt.axis('off')
plt.show()
#fig.savefig('CHTO PROISHODIT.png', transparent=False, dpi=80, bbox_inches="tight")