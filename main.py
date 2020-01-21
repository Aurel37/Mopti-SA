from generation_matrice import w
from temps_arret import moyenne_ta

Test = True

if Test:
    try:
        Test = 3
    except False:
        print("Test n'est pas un entier")
    except True:
        print("Test est un entier")




print(moyenne_ta(10, 30,  0.5, 0.1, 1, w))
