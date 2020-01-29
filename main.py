from temps_arret import main
import numpy as np
import matplotlib.pyplot as plt
from generation_matrice import gen_matrix, w

N = 30
l = 0.5
dt = 0.0001
ntests = 1000

X = [i for i in range(1, 5)]
Y = [i for i in range(1, 5)]
Yerr = []
graph = gen_matrix(N, w)
print(X)
for i in range(len(X)):
    print(i)
    res = main(N, ntests, l*dt, dt, graph, X[i])
    Y[i] = res[0]
    Yerr.append(res[1])

plt.errorbar(X, Y, Yerr)
plt.show()
