#Dans ce chapitre nous allons voir comment pouvoir recupérer les clés d'un dict
#par la meilleur de facon.

my_dict = {'Mamadou': 'Boutiquier',
           'Thierno':'Menuisier',
           'Alpha': 'Professeur'}

'''Dans l'exemple qui suit, nous allons voir comment recupérer les clés de my_dict
sans avoir une erreur même si le clé n'existait pas.'''
#Avec erreur si la clé n'existe pas
#Dans cette exmple on aura une erreur car le nom Oumar ne pas une clé dans my_dict
#perso_cles = my_dict['Oumar']
#print(perso_cles)

#Empêcher que le script de planter même si Oumar n'existait pas dans my_dict
#On recherche la clé, si elle n'existe pas, on affiche un message, qu'on renseigne en 2em param
perso_cles1 = my_dict.get('Oumar', "Oumar n'existe pas dans le dictionnaire.")
print(perso_cles1)