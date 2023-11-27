#Les sets en python

'''Les Sets permettent de contenir d'autres type de donnés dites immuables
comme par exemple les INT, String, Tuple, mais les Sets ne peut pas contenir les listes et dictionnaires
car ces donnés sont des types muables'''

my_list = [34, 89, 'Diallo', 'Sow']
#Declaration d'un set

my_sets = {1,2,3,3,4, 4, 4,5, 'Mamadou',10, 'Abdoul', (1, 'BASSIR')}
print(my_sets)
'''On peut ajouter les donnés d'une liste dans un set, mais pas la liste elle même
Dans l'exmple suivant à l'aide de la méthode update() on ajoute les données de my_list dans my_sets
'''
my_sets.update(my_list)
print(my_sets)
#On peut supprimer un élement de la set à l'aide de la fonction  remove()
#Pour celá, il faudra renseigné le nom de l'élément à supprimer
my_sets.remove('Sow')
print(my_sets)

'''Il faut savoir aussi qu'un set n'accpete pas  le doublon
 
 Dans l'exemple en-bas, un de 2, un de 3 et un de Mamadou seront automatiquement supprimé'''
anothes_set = {1, 2, 2, 3, 3, 4, 'Mamadou', 'Mamadou', 'Bassir'}
print(anothes_set)

'''
Un autre utilité des Sets et sa capacité à faire des calcules poussés
Dans les exmples suivants on va voir comment utiliser les Sets pour 
faire des calcules d'UNION, D'INTERSECTION, de DIFFERENCE et de DIFFERENCE SYMETRIC'''

groupe_a = {1, 2, 3, 4, 5}
groupe_b = {4, 5 ,6 ,7, 8}
prenoms_a ={'Mamadou', 'Alpha', 'Ismael', 'Ibrahim', 'Souleymane'}
prenoms_b = {'Souleymane', 'Abdoul', 'Ibrahim', 'Alpha', 'Ismael'}
print('--'*20,'\n',)
#Calcul d'UNION
#On prend tous les nombres et les personnes qui sont dans groupe_a et en même temps dans groupe_b
union_nombre = groupe_a.union(groupe_b)
list_perso = prenoms_a.union(prenoms_b)
print(union_nombre)

print(list_perso)
print('--'*20,'\n',)

#Calcul Différence Symétric
#On prend les nombres et personnes qui ne sont pas en meme temps dans les deux groupes
diff_symetric = groupe_a.symmetric_difference(groupe_b)
diff_perso_symetric = prenoms_a.symmetric_difference(prenoms_b)
print(diff_symetric)

print(diff_perso_symetric)

#Calcul d'intersection
#On prend seulement les noms et nombres qui sont dans les deux groupes en même temps

intersection_nombres = groupe_a.intersection(groupe_b)
intersection_perso = prenoms_a.intersection(prenoms_b)
print('--'*20,'\n', intersection_nombres)
print(intersection_perso)

#Calculde difference
#On prend la différence de a dans b, exemple: tous les persones qui sont dans a mais pas dans b
diff_nombres = groupe_a.difference(groupe_b)
diff_perso = prenoms_a.difference(prenoms_b)
diff_b_dans_a = prenoms_b.difference(prenoms_a)
print('-'*20, '\n',diff_nombres)
print(diff_perso)
print(diff_b_dans_a)

#Un autre exemple d'utilisation des Set, pouvoir savoir si un element se trouve dans un ensemble
print('Mamadou' in my_sets)

"""
En résumé, les ensembles en Python sont utiles lorsque vous avez besoin de gérer une collection d'éléments uniques,
 de supprimer les doublons,
  de tester rapidement l'appartenance et de réaliser des opérations ensemblistes.
"""

