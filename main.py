from temps_arret import main
import numpy as np
import matplotlib.pyplot as plt
from generation_matrice import gen_matrix, w

N = 30
l = 0.5
mu = 0.2
dt = 1
ntests = 1000

X = [i for i in range(1, 10)]
Y = [i for i in range(1, 10)]
graph = gen_matrix(N, w)
print(X)
for i in range(len(X)):
    print(i)
    Y[i] = main(N, ntests, l*dt, mu*dt, graph, X[i])
plt.plot(X, Y)
plt.show()


