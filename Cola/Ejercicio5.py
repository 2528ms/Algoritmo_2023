# 5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.


#Import file since other folder
import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Pila') #add path the folder
import pilaClass #select file that contain of folder added

from colaClass import Cola
from random import randint

cola = Cola()
pila_aux = pilaClass.Pila()


for i in range(5):
    pila_aux.push(randint(0,50))

print('Pila Original')
while pila_aux.size() > 0:
    print(pila_aux.on_top())
    cola.arrive(pila_aux.pop())

while cola.size() > 0:
    pila_aux.push(cola.atention())

print('Pila invertida')
while pila_aux.size() > 0:
    print(pila_aux.pop())