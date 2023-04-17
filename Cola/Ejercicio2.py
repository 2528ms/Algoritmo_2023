"""
Ejercicio: Utilizando operaciones de cola y pila, invertir el contenido de una cola
se deberia sacar(eliminarlo) desde una cola ya cargada, el valor de la primera pocicion e insertarlo en una pila,
luego sacar el valor que esta en la cima de la pila e insertarlo nuevamente en la cola
"""
#Import file since other folder
import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Pila') #add path the folder
import pilaClass #select file that contain of folder added

from colaClass import Cola
from random import randint

cola = Cola()
pila = pilaClass.Pila()

for i in range(4):
    valor = randint(0,20)
    cola.arrive(valor)
    print(valor)
    
print("***************")
while cola.size() > 0:
    valor = cola.atention()
    pila.push(valor)
    print(valor)

print("***************")
while pila.size() > 0:
    valor = pila.pop()
    cola.arrive(valor)
    print(valor)

