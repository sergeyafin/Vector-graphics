import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 9))
ax0 = fig.add_subplot()
#  X = np.arange(7)
X = np.array([0, 1, 2, 3, 4, 5, 6])

#  Y = np.arange(7)
Y = np.array([0, 1, 2, 3, 4, 5, 6])

#  U = np.repeat([4,3,2,1,2,3,4], 7).reshape(7, 7)
U = np.array([[4, 4, 4, 4, 4, 4, 4],
              [3, 3, 3, 3, 3, 3, 3],
              [2, 2, 2, 2, 2, 2, 2],
              [4, 4, 4, 4, 4, 4, 4],
              [2, 2, 2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4, 4, 4]])

#  V = np.repeat([1,2,3,4,3,2,1], 7).reshape(7, 7)
V = np.array([[100, 100, 100, 100, 100, 100, 100],
              [-200, 200, -200, 200, -200, 200, -200],
              [3, 3, 3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4, 4, 4],
              [3, 3, 3, 3, 3, 3, 3],
              [2, 2, 2, 2, 2, 2, 2],
              [1, 1, 1, 1, 1, 1, 1]])
fig, axes = plt.subplots()
u1=500-(-100)*np.random.random((7,7))-500
v1=1500-(-100)*np.random.random((7,7))-1600
u2=100-(-100)*np.random.random((7,7))-100+3
v2=100-(-100)*np.random.random((7,7))-100
axes.streamplot(X, Y, u1,v1, color=u1+v1,density=2,maxlength=0.4,linewidth=2-u1/v1,arrowstyle = "->")
axes.streamplot(X, Y, u2,v2, color=u2+v2,density=1.5)
#axes[1].streamplot(X, Y, u2,v2 , color="gold", linewidth=4-u2/v2,arrowsize=0.1)


fig.set_figwidth(8)    #  ширина и
fig.set_figheight(8)    #  высота "Figure"
plt.grid(b=False)
plt.axis('off')
plt.show()
#fig.savefig('CHTO PROISHODIT.png', transparent=False, dpi=80, bbox_inches="tight")