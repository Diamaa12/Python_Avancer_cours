#Dans ce chapitre nous allons voir les erreurs recurrente à éviter avec Python
import random


# 1. Ne jamais passé une liste vite dans une fonction comme ceci
def my_fonction(my_list=[]):
        my_list.extend([random.randint(1, 20) for i in range(5)])
        return my_list
for i in range(5):
    print(my_fonction())


#Passer toujour par l'exemple suivant

def my_fonction2(my_list=None):
    if my_list is None:
        my_list = []
        my_list.extend([random.randint(1, 20) for i in range(5)])
        return my_list
'''Dans cette exemple de fonction, au lieu d'incrérementer une liste
qu'on aurait passé à la fonction, à chaque appel de la fonction on crée une novelle liste'''
for i in range(5):
    print(my_fonction2())

#Recuperer l'index d'une liste sans erreur avec le bloc try except

my_index = ['Mamadou',2, 3, 12.4, 5, 6]
print(my_index.index(12.4))
#Là on aura une erreur, car le nom Ibrahim n'est pas dans la liste
#print(my_index.index('Ibrahim'))
#Pour eviter cette erreur, on va utilisé une bloc try except
try:
     perso = my_index.index('Ibrahim')
     print(perso)
except ValueError:
    print('L index n existe pas.')
