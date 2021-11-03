from random import *

pocet = int(input('Zadaj počet hesiel:'))

def nahodne_heslo(subor):
    heslo = ''
    for i in range(8):
        heslo += chr(randint(97, 122))
    print(heslo, file=subor)

subor = open('hesla.txt', 'w')
for i in range(pocet):
    nahodne_heslo(subor)
subor.close()

