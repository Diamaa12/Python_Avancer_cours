#Dans ce chapitre, nous allons étudier les args et kwargs
import os
import pathlib
import shutil
import sys
from pprint import pprint

from PySide6 import QtWidgets
'''Pour comprendre les args et kwargs, il faut comprende l'idée de unpacking
'''

'''Dans l'exemple suivant nous allons voir c'est quoi le unpacking'''
class MyClasse(QtWidgets.QWidget):
    def __init__(self, test):
        super().__init__()

        #Ici on crée trois parametres qu'on passe par la suite à la fonction format() avec les deux étoiles avant le non de variable
        couleur_bouton = {'rouge':255, 'vert':0, 'bleu':0}
        self.btn = QtWidgets.QPushButton('My Button')
        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.btn.setStyleSheet('background-color:rgb({rouge},{vert},{bleu}'
                               ')'.format(**couleur_bouton))

        self.main_layout.addWidget(self.btn)

        self.btn.clicked.connect(self.close)

# app = QtWidgets.QApplication()
# win = MyClasse('click')
# win.show()
# sys.exit(app.exec())

#Autre exemple de Args

'''Dans l'exemple suivant, on crée une fonction liste_invitee()
on passe à la fonction un parametre invite_vip, et un *args
le args contient d'autres paramétres, ici la liste des invitées normaux
on affiche l'invité vip contenu dans le parametre de la fonction (invite_vip)
Au moment d'appel de la fonction, le premier nom donné, sera l'invité VIP
les autres noms qui suivent seront rangée dans le *args et seront considéré comme
étant les invité normaux
'''
def liste_invitee(invite_vip, *args):
    #Invité VIP
    print("{} est un invite VIP".format(invite_vip))
    #On fait une boucle pour afficher le nom de tous les autres invités normaux
    for invite in args:
        print('{} est un invité Normal'.format(invite))
#On appel la fonction, avec les noms des invités
#La premiére personne sur la liste sera considérer comme étant le VIP
#Les autres noms seront rangé dans le *args et seront les invités normaux
liste_invitee('Mamadou', 'Samed', 'Pedro', 'Leon', 'Samuel')

'''Un autre exemple de args'''
def additon(multiplier, *args):
    #on fait la somme de tous les nombres contenu dans args et on les retourne
    return multiplier * sum(args)
'''On appel la fonction addition() avec un premier paramétre
On multiplie le premier paramétres avec la somme de tous les autres nombres'''
print(additon(5,2,3,4,6,10))

'''Les kwargs prennent le nom de la valeur passé en paramétre.'''
def lieu_de_naissance(sous_prefecture, *args, **kwargs):
    print(f"{sous_prefecture}")
    #On recupére les clés de dictionnaire **kwargs
    quartier = kwargs.get('quartier')
    quartier2 = kwargs.get('quartier2')
    quartier3 = kwargs.get('quartier3')
    #on boucle sur le args en recupérant les valeurs de celci et on les mettent dans distric
    for distric in args:
        print(f"La sous-prefecture de {sous_prefecture} est composé de : {distric}")
        if distric == 'bombi_bourou':
            print('Les quartiers de BBourou sont:{}'.format(', '.join(quartier)))
        elif distric == 'Horebombi':
            print('Les quartiers de Horebombi sont:{}'.format(', '.join(quartier2)))
        else:
            print('Les quartiers de Zawia sont:{}'.format(', '.join(quartier3)))


#On appel la fonction avec les args et kwargs
lieu_de_naissance('Lafou','bombi_bourou', 'Zawia', 'Horebombi', quartier=['Leyssare','Kowli','Galle'],
                                                                                         quartier2=['Leybolol', 'Pelel', 'Thiewghel', 'Dowwho'],
                                                                                         quartier3=['Dowsaaré', 'Hindhé', 'Bholie'])

'''Un autre exemple de args et kwargs'''
def fils_manager(dossier, *files, **extenstions):
    print('Le dossier est {}'.format(dossier))
    items = extenstions.get('extensions')
    print(type(items))
    for ele in files:
        print(type(ele))
        #pprint(ele)
        path = dossier / ele
        if not path:
            path.mkdir()
        else:
            if ele == 'PDF':
                for item in items:
                    if item.endswith('.pdf'):
                        p = dossier / ele
                        d = pathlib.Path('/home/bombilafou/Téléchargements')
                        dirctory = d / item
                        if shutil.copy2(dirctory, p):
                            print(f"p {dirctory} copié vers >>> {p}")
                        else:
                            print('Un probléme est survenu !')
            if ele == 'PNG':
                for item in items:
                    if item.endswith('.png'):
                        print(item)
            if ele == 'JPEG':
                for item in items:
                    if item.endswith('.jpg'):
                        print(item)







dossier = pathlib.Path('/home/bombilafou/Documents/Test_docs')
fichiers = pathlib.Path('/home/bombilafou/Téléchargements')

#print(fichiers)
files = []
if os.path.isdir(fichiers):
    mes_fichiers = [f for f in os.listdir(fichiers) if os.path.isfile(os.path.join(fichiers,  f))]
    #pprint(mes_fichiers)
    files.extend(mes_fichiers)



fils_manager(dossier,'PNG','JPEG',  'PDF','TEXT' , extensions=files)
