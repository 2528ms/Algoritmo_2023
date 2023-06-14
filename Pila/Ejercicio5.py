# 5. Determinar si una cadena de caracteres es un palíndromo

from pilaClass import Pila

stack = Pila()
stack_aux = Pila()

word_invertida = ''
resultado = True
word = input('ingrese pasabra ')

#Cargamos la pila principal con la cadena ingresada
for i in word:
    stack.push(i)

#vamos cargando la pila aux con el ultimo caracter de la cadena
while word:
    value = word[-1]
    stack_aux.push(value)
    word = word[:-1]
    

while stack.size() > 0:
    if (stack.pop() != stack_aux.pop()):
        resultado = False

# while stack.size() > 0:
#     word_invertida += stack.pop()

if resultado:
    print('La palabra ingresada es un palindromo')
else:
    print('La palabra ingresada NO es un palindromo')