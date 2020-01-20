from temps_arret import main
import numpy as np
import matplotlib.pyplot as plt
from generation_matrice import gen_matrix, w

N = 30
X = np.linspace(0.2, 0.5, 20)
Y = np.linspace(0.2, 0.5, 20)
graph = gen_matrix(N, w)
for i in range(1):
    Y[i] = main(N, 10, 0.5, X[i], graph)
plt.plot(X, Y)
plt.show()


