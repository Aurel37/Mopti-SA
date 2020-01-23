from temps_arret import main
import numpy as np
import matplotlib.pyplot as plt
from generation_matrice import gen_matrix, w

N = 30
l = 0.3
dt = 0.01
ntests = 1000

X = [i for i in range(1, 5)]
Y = [i for i in range(1, 5)]
graph = gen_matrix(N, w)

for i in X:
    print("i")
    Y[i] = main(N, ntests, l*dt, dt, graph, i)
plt.plot(X, Y)
plt.show()


