# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
# meros pares.
from pilaClass import Pila
from random import randint

stack = Pila()
stack_aux = Pila()

#! Carga
for i in range(14):
    valor = randint(0,100)
    print('valor generado', valor)
    stack.push(valor)

#! Sacamos el ultimo valor de la pila y verificamos is es par o no
while stack.size() > 0:
    valor = stack.pop()
    if valor % 2 == 0:
        stack_aux.push(valor)

#!
while stack_aux.size() > 0:
    #valor = stack_aux.on_top()
    #stack.push(valor)
    stack.push(stack_aux.pop())




while stack.size() > 0:
    valor = stack.pop()
    print('El valor que queda es: ', stack.pop())
    #print(stack.pop())




