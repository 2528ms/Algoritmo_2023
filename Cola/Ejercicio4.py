#Ejercicio 4: Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos

from colaClass import Cola
from random import randint
cola = Cola()

print("******Cola original*********")
for i in range(5):
    valor = randint(0,20)
    cola.arrive(valor)
    print(valor)
    

def es_primo(numero):
    contador = 0
    for i in range(2,numero):
        if numero % i == 0:
            contador += 1
            break
    return contador == 0

cont = 0
tamanioActual = cola.size()
while cont < tamanioActual:
    if es_primo(cola.on_front()):
        cola.move_to_end()
    else:
        cola.atention()        
    cont += 1

print("***************")
print(f'el tamanio es: {cola.size()} luego de eliminar los num que NO son primos')
print("******Cola Resultante*********")

while cola.size() > 0:
    print(cola.atention())
    


