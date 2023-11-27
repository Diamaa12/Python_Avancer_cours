#Une fonction anonyme est une fonction qu'on utilise qu'une fois
#et qu'on a pas besoin de reutiliser par la suite
import os
from pathlib import Path
from pprint import pprint
from PySide6 import QtWidgets
import sphinx
#Exemple de la fonction lambda qui attende des arguments en parametre.

ma_fonction = lambda x, y: y*x
resultat = ma_fonction(7, 7)

print(resultat)

#Une fonction lambda qui n'attend aucun argement
print_contenu = lambda: print('Salam')
print_contenu()

#Une fonction qui attend un seule argument
print_argument = lambda m: print(m)
print_argument('Leyssare')

#Exemple d'utilisation avancée de lambda

fichiers = Path().cwd()
list_fichiers = []
for p in fichiers.rglob('*.py'):
    print(p.name)
    list_fichiers.append(p)
pprint(list_fichiers)

#Ici on va trier les fichiers de cet tableau et retourner l'extention à l'aide de lambda
get_fichier = lambda f: os.path.split(f)[-1]
get_extention = lambda f:os.path.splitext(f)[-1]
del_point = lambda f: f.replace('.','')
process = lambda f:del_point(get_extention(get_fichier(f)))
print(get_fichier)
extentions = [process(f) for f in list_fichiers]
print(extentions)
#Un autre exemple d'utilisation de lambda dans le trie par ordre alphabetique d'une liste

users = [('User1','Mamdou'),
         ('User2','Abdoul'),
         ('User3', 'Alghassim'),
         ('User4', 'Bassir'),
         ('User5', 'Mouktar')]
users.sort(key=lambda x: x[1]) #Ici on veut que le tuple soit trier en tenant compte de la deuxiéme valeur du tuple (valeur1, valeur2)
pprint(users)
#Dans le dernier cas l'utilisateur Abdoul sera le premier à être afficher
class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 400, 50, 50)
        self.setWindowTitle('My Fenster')

        self.btn_valider = QtWidgets.QPushButton('Valider')
        self.btn_annuler = QtWidgets.QPushButton('Annuler')

        self.lbl_un = QtWidgets.QLabel('Nombre1:')
        self.le_un = QtWidgets.QLineEdit()

        self.lbl_deux = QtWidgets.QLabel('Nombre2:')
        self.le_deux = QtWidgets.QLineEdit()

        self.lbl_resultat = QtWidgets.QLabel('Resultat:')
        self.resultat = QtWidgets.QLineEdit()

        self.mai_layout = QtWidgets.QHBoxLayout(self)
        self.add_widget_to_layout()
        self.connect_widget()
        #self.calcul()

    def add_widget_to_layout(self):
        self.mai_layout.addWidget(self.btn_valider)
        self.mai_layout.addWidget(self.btn_annuler)
        self.mai_layout.addWidget(self.lbl_un)
        self.mai_layout.addWidget(self.le_un)
        self.mai_layout.addWidget(self.lbl_deux)
        self.mai_layout.addWidget(self.le_deux)
        self.mai_layout.addWidget(self.lbl_resultat)
        self.mai_layout.addWidget(self.resultat)

    def connect_widget(self):
        #Exemple d'utilisation des Lambda avec Pyside
        self.btn_valider.clicked.connect(lambda: self.afficher_mot('Salut'))
        self.btn_annuler.clicked.connect(lambda: self.afficher_mot('Au revoir'))

        #Grace à lambda, on recupere le text de deux LineEdit
        #on les transforme en int, on fait l'addition
        #et on passe le resultat de l'addtion à self.resultat.setText()
        self.le_deux.returnPressed.connect(lambda : self.resultat.setText(str(int(self.le_un.text())+int(self.le_deux.text()))))
        #self.le_deux.returnPressed.connect(lambda : self.calcul(self.le_deux.text()))
    def afficher_mot(self, mot):
        print(mot)


my_app = QtWidgets.QApplication()
window = MyApp()
window.show()
window.setGeometry(300, 250, 200, 300)
my_app.exec()

