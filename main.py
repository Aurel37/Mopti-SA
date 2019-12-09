from generation_matrice import w, gen_matrix
from temps_arret import moyenne_ta

N = 30
X = [True for i in range(N)]
graph = gen_matrix(N, w)
print(moyenne_ta(10, N,  0.1, 0.1, X, graph))
