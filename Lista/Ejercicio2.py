#Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

from listaClass import Lista
from random import randint

caracteres = Lista()

for i in range(20):
    caracteres.insert(chr(randint(65, 90)))

print('Lista original de caracteres, tamaño', caracteres.size())
caracteres.barrido()

for i in range(caracteres.size()):
    if caracteres.get_element_by_index(i) in ['A','E','I','O','U']:
        caracteres.delete(caracteres.get_element_by_index(i))

print('Lista de caracteres sin vocales, tamaño', caracteres.size())
caracteres.barrido()
