import random

def generer_liste_aleatoire(taille):
    return [[random.randint(1, 1000) for e in range(taille)] for i in range(taille)]

def moyenne(listes):

    somme_comparaisons = 0
    somme_permutations = 0

    for i in listes:
        c,p = tri_bulle(i)
        somme_comparaisons += c
        somme_permutations += p

    return somme_comparaisons/len(listes), somme_permutations/len(listes)


def tri_bulle(liste):
    n = len(liste)
    permutation_effectuee = True
    comparaisons = 0  
    permutations = 0  

    for i in range(n):
        permutation_effectuee = False
        for j in range(0, n-i-1):
            comparaisons += 1  # Incrémenter le compteur de comparaisons
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                permutation_effectuee = True
                permutations += 1  # Incrémenter le compteur de permutations
        if not permutation_effectuee:
            break
        
    return  comparaisons, permutations

"""
liste = [12, 17, 14, 11, 8]
liste_triee, nb_comparaisons, nb_permutations = tri_bulle(liste)
print("La liste triée est:", liste_triee)
print("Nombre de comparaisons effectuées:", nb_comparaisons)
print("Nombre de permutations effectuées:", nb_permutations)
"""

m1,m2, = moyenne(generer_liste_aleatoire(100))
print("moyenne comparaisons:", m1)
print("moyenne permutations:", m2)