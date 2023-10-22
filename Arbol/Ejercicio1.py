# Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

from TP5.binaryTree import BinaryTree
from random import randint

arbol = BinaryTree() #instanciamos un nuevo Tree
test = [] 

#Insertamos 20 numeros enteros entre el 0 y el 100
for i in range(6):
    value = randint(0,100)
    test.append(value)
    arbol.insert_node(value)


print('Valores insertados') 
for elemento in test:
    print(elemento)
print('Barrido In Orden - Imprime los valores de forma descendiente')
arbol.inorden()
print()
print('Valores insertados') 
for elemento in test:
    print(elemento)
print('Barrido pre Orden')
arbol.preorden()
print(test)
print()
print('Valores insertados') 
for elemento in test:
    print(elemento)
print('Barrido post Orden - Imprime los valores de forma ascendiente')
arbol.postorden()

print(test)