#Dada una lista de números enteros eliminar de estas los números primos.

from listaClass import Lista
from random import randint

lista_numeros = Lista()

for i in range(10):
    lista_numeros.insert(randint(1, 100))

print('Lista original de numeros, tamaño', lista_numeros.size())
lista_numeros.barrido()

def es_primo(numero):
    primo = False
    for i in range(2,numero):
        if numero % i == 0:
            primo = True
            break
    return primo == False

cont = 0 

while cont < lista_numeros.size():
    if es_primo(lista_numeros.get_element_by_index(cont)):
        lista_numeros.delete(lista_numeros.get_element_by_index(cont))
        cont += 1
    cont += 1

print('Lista de numeros sin numeros primos, tamaño', lista_numeros.size())
lista_numeros.barrido()
