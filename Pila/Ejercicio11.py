# 11. Dada una pila de letras determinar cuántas vocales contiene.

from random import randint
from pilaClass import Pila

stack = Pila()
vocales = ['A','E','I','O','U']
cantVocales = 0

for i in range(20):
    valor = chr(randint(65, 90))
    stack.push(valor)
    #print('aleatorios ',valor)

while stack.size() > 0:
    if stack.pop() in vocales:
        cantVocales += 1 


print('Total de vocales ',cantVocales)

