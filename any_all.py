#Les fonctions any et all en python

'''Dans cette exemple on veut savoir si dans la liste
tous les personnes ont une âge égal ou superieur à 18 '''
import pathlib
import shutil
from pprint import pprint

age_inviter = [17, 16, 15, 17, 18, 14]
reponse = all([i >= 18 for i in age_inviter])
print(reponse)

'''Dans cette exemple on veut savoir si dans la liste
y a au moins une personne dont l'âge est superieure ou égal à 18 ans'''
reponse2 = any(i >= 18 for i in age_inviter)
print(reponse2)

# path = pathlib.Path('/home/bombilafou/Téléchargements')
# extentions = [p for i, p in enumerate(path.rglob('*.sql'))]
# pprint(extentions)
# direct_to_move = pathlib.Path('/home/bombilafou/Documents/SQL')
# for ele in extentions:
#     if ele.is_file():
#         shutil.copy(ele, direct_to_move)
#         print

'''Ici on veut voir si tous les donnés dans notre tableu sont
False, et ici la fonction all() renvera False, car tous le contenu 
du Tableu est False'''
r1 = all([False, False, False, False])
'''Ici on veut voir si tous les donnés dans notre tableu sont
False, et ici la fonction all() renvera False, car tous le contenu 
du Tableu n'est pas False'''
r2 = all([False, False, True, False])

'''Ici on veut voir si tous les donnés dans notre tableu sont
True, et ici la fonction all() renvera True, car tous le contenu 
du Tableu est True'''
r3 = all([True, True, True, True])

'''Avec la fonction any(), on a un moyen de savoir si au moins
une personne dans la liste a plus de 18 ans, la fonction any() renvera False'''
age_perso = [17, 15, 14, 13, 16]
rst1 = any(majeur >= 18 for majeur in age_perso)

'''Ici la fonction renvera True, car y a au moyen une persone
qui est a plus de 18 ans'''
age_perso1 = [17, 15, 14, 13, 16, 20, 21]
rst2 = any(majeur >= 18 for majeur in age_perso1)

print(r1, r2, r3, rst1, rst2)


'''La fonction all() renverra false si tout le contenu du tableau est False
    La fonction all() renverra True si tout le contenu du tableau est True
    La fonction all() renverra False si dans un tableu de True y a un False de dans
    La fontion all() renverra False si dans un tableau de False y a un true
    '''
'''La fonction any() verifie si un valeur se trouve dans un tableau
    Si oui, la fonction renvera True, si non, la fonction renverra False
    '''

#Exemple un peut pousser de l'utilisation de ces deux fonctions
fichiers = ['C:/dossier_test/fichier01.jpg',
			'C:/dossier_test/fichier02.tif',
			'C:/dossier_test/fichier03.png',
			'C:/dossier_test/fichier04.jpg',
			'C:/dossier_test/fichier05.jpg']

au_moins_un_png = any(x.endswith('.png') for x in fichiers)
tous_des_jpg = all(x.endswith('.jpg') for x in fichiers)
print(au_moins_un_png, tous_des_jpg)