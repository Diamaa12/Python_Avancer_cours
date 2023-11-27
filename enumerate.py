#Comprendre la fonction enumerate
'''La fonction enumerate permet de recupérer
le numéro et l'element dans une liste

 Et quand on passe un deuxiéme paramétre à la fonction,cela permet
 à ce que la liste commence au numéro renseigné en paramétr
 exp: au lieu de commencer à zéro comme toute liste python,
 on peut décaler l'index au numéro passé en parametre '''

liste_noms = ['Mamadou', 'Alpha', 'Bassir', 'Safiatou']
for i, noms in enumerate(liste_noms, 1):
    print('Employer no ', i, ' ', noms)

dict_perso = {'Pays': 'Senegal',
              'Nom':'Mamadou',
              'Addresse':'Dakar'}

for i, (cle, valeur) in enumerate(dict_perso.items(), 7):
    print(f"{i}, {cle} {valeur}")



