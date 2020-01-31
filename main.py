from temps_arret import main
import numpy as np
import matplotlib.pyplot as plt
from generation_matrice import gen_matrix, w

N = 30
l = 0.5
mu = 0.2
dt = 0.01
ntests = 100


X = [i for i in range(1, 5)]
Y = [i for i in range(1, 5)]
Yerr = []

graph = gen_matrix(N, w)
print(X)
for i in range(len(X)):
    print(i)
    res = main(N, ntests, l*dt, mu*dt, graph, X[i])

    Y[i] = res[0]
    Yerr.append(res[1])
 
plt.errorbar(X, Y, Yerr)
plt.show()
