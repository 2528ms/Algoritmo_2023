# Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

from binaryTree import BinaryTree
from random import randint

arbol = BinaryTree()
test = []
for i in range(15):
    value = randint(0,100)
    test.append(value)
    arbol.insert_node(value)


print()
for elemento in test:
    print(elemento)
print('Barrido In Orden')
arbol.inorden()
print()
for elemento in test:
    print(elemento)
print('Barrido pre Orden')
arbol.preorden()
print()
for elemento in test:
    print(elemento)
print('Barrido post Orden')
arbol.postorden()