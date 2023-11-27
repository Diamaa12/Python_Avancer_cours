#Dans ce chapitre nous allons voir les operations ternaires en Python
from pprint import pprint

#import debogging
age = 17
if age >= 18:
    print('vous êtes majeur')
else:
    print('Vous êtes mineur')

'''avec les ternaires ca donne ce qui suit'''

person = 'Vous êtes majeur' if age >= 18 else 'Vous êtes mineur'
print(person)

# nmr = int(input('Taper un nombre'))
# nmbr_positif = True if nmr > 0 else False
# print(nmbr_positif)

pprint(dir(''))

