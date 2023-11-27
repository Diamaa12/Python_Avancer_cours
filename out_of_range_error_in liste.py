#ici nous allons voir comment éviter l'erreur Out of range quand on veut supprimer
#élément danns une liste

ma_liste = ['Mamadou', 'Alpha', 'Bhoye', 'Kadidiatou']
#Maintenant nous allons vouloir supprimer Alpha dans notre liste, en faisant une boucle sur la liste
# for nom in range(len(ma_liste)):
#     if ma_liste[nom] == 'Alpha':
#         '''L'erreur ici sera le fait que la longeur de notre liste était 3 au départ
#         et quand on supprime Alpha, il ne restera plus que 3 èlement de 0, 1, 2 et donc le 3 sera supprimer
#         mais comme au debut, on avait qautre valeur, la boucle tentera d'atteindre le quatriéme valeur
#         qui lui n'existe plus, car supprimé déjà
#         La meilleur facon de faire une supprison d'un valeur dans une liste, c'est de passé par
#         les compréhension des listes'''
#         del ma_liste[nom]
#         print(nom)

#Meilleur facon de faire
liste_sans_alpha = [ele for ele in ma_liste if ele != 'Alpha']
'''Dans cette facon de faire, on crée une autre liste sans la personne, et on est sûr qu'il y aura pas d'erreur'''
print(liste_sans_alpha)