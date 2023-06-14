# 8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
# cartas de baraja española–,resolver las siguientes actividades:
# a. generar las cartas del mazo de forma aleatoria;
# b. separar la pila mazo en cuatro pilas una por cada palo;
# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

from pilaClass import Pila

def cargar_carta(stack, carta):
    pila_aux = Pila()
    if stack.size() == 0 or stack.on_top() <= carta:
        print('apilar carta', carta)
        stack.push(carta)
    else:
        while stack.size() > 0 and stack.on_top() > carta:
            carta_aux = stack.pop()
            print('cambiar carta de maso temporalmente', carta_aux)
            pila_aux.push(carta_aux)
        stack.push(carta)
        while pila_aux.size() > 0:
            stack.push(pila_aux.pop())



cartas = [12, 5, 1, 10, 3, 7]

pila_principal = Pila()



for carta in cartas:
    cargar_carta(pila_principal, carta)
    input()


while pila_principal.size() > 0:
    print(pila_principal.pop())