#La comprehensio des listes en Python

'''Exemple de multiplication de valeur d'un liste par un nombre'''
from pprint import pprint

liste = [1, 2, 3, 4, 5, 6, 7, 8]
print(id(liste))
liste1 = [i*2 for i in liste]
print(id(liste1))

'''Dans l'exemple suivant on multiplie les vleurs de la liste par 2
si le nombre est pair'''

liste_pair = [i*2 for i in liste if i % 2 == 0]
print(liste_pair)

'''Un autre exemple avec les conditions else if
dans cette exemple on multiplie les valeurs pairs de la liste en deux
si les valeurs sont impaires on leur multiplie par 3
'''
liste_condition = [i*2 if i % 2 == 0 else i*3 for i in liste]
print(liste_condition)

#Exercice
liste_exercice = [10, 11, 12, 13, 14, 15, 16, 17, 18]
m_par_deux = [i*2 for i in liste_exercice]
print(m_par_deux)

un_autre_liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
par_trois = [i*3 for i in un_autre_liste if i > 0]
print(par_trois)

liste_if_else = [i*3 if i > 0 else i / 3 for i in un_autre_liste]
print(liste_if_else)

liste_finale = [(a, b) for a in range(10) for b in range(10)]
pprint(liste_finale)
