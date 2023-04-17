#Import file since other folder
import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Pila') #add path the folder
import pilaClass #select file that contain of folder added

from colaClass import Cola
from random import randint

cola = Cola()
pila = pilaClass.Pila()

word = input("enter a word ")

for i in range(len(word)):
    value = word[i]
    cola.arrive(value)
    print(value)

print('***************************')    
size = cola.size()
cont = 0

while cont < size:
    value = cola.on_front()
    cola.move_to_end()
    pila.push(value)
    cont += 1
    print(value)

print("*************************************")
palindroma = True
while pila.size() > 0:
    valueStack = pila.pop()
    valueCola = cola.on_front()
    cola.move_to_end()
    print(f'La comparasion es: en cola {valueCola} con pila {valueStack}')
    if valueCola != valueStack:
        palindroma = False

print("*************************************")
if palindroma:
    print(f'La palabra "{word}" ingresada es palindroma')
else: 
    print(f'La palabra "{word}" NO es palindroma')
