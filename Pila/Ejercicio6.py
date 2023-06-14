# 6. Leer una palabra y visualizarla en forma inversa.
from pilaClass import Pila

cadena = input('ingrese palabra: ')
cadena_invertida = ''
stack = Pila()

for i in cadena:
    stack.push(i)

while stack.size() > 0:
    #print(stack.pop())
    cadena_invertida = cadena_invertida + stack.pop()

print(f'la palabra ingresada es {cadena} invertida queda: {cadena_invertida}')
    

