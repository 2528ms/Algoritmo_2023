"""
Ejercicio: Utilizando operaciones de cola y pila, invertir el contenido de una cola
se deberia sacar(eliminarlo) desde una cola ya cargada, el valor de la primera pocicion e insertarlo en una pila,
luego sacar el valor que esta en la cima de la pila e insertarlo nuevamente en la cola
"""

#from AlGORITMO_2023_MS.Pila.pilaClass import Pila
import Pila.pilaClass
from colaClass import Cola
from random import randint

cola = Cola()
pila = Pila()

for i in range(10):
    valor = randint(0,20)
    cola.arrive(valor)
    print(valor)
    


