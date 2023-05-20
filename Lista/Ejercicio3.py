from random import randint
from listaClass import Lista

listaValores = Lista()
listaPar = Lista()
listaImpar = Lista()

for i in range(15):
    listaValores.insert(randint(1,50))

for i in range(listaValores.size()):
    value = listaValores.get_element_by_index(i)
    if value % 2 == 0:
        listaPar.insert(value)
    else:
        listaImpar.insert(value)

print('****** Lista de valores ******')
listaValores.barrido()
print('****** Lista de valores pares ******')
listaPar.barrido()
print('****** Lista de valores impares ******')
listaImpar.barrido()