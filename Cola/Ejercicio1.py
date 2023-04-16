from colaClass import Cola
from random import randint

cola = Cola()

for i in range(0,10):
    chart = chr(randint(65,90))
    cola.arrive(chart)
    print(chart)

print("tamaño final ", cola.size())
print("*********************************************")
vowels = ["A","E","I","O","U"]
sizeCurrent = cola.size()
cont = 0
while cont < sizeCurrent:
    currentChart = cola.on_front()
    print(currentChart)
    if currentChart in vowels:
        cola.atention()
    else:
        cola.move_to_end()
    cont += 1

print("tamaño final ", cola.size())
print("*********************************************")
while cola.size() > 0:
    valor = cola.atention()
    print(valor)

print("tamaño final ", cola.size())