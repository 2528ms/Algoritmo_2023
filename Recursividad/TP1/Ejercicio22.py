"""El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;
c. Utilizar un vector para representar la mochila
"""

mochila = ["sable","cartuchera","lapicera","sable de luz","campera","billetera"]

def usar_la_fuerza(lista, buscado):
    if len(lista) == 0:
        return -1
    elif lista[-1] == buscado:
        return len(lista)-1
    else:
        return usar_la_fuerza(lista[0:-1], buscado)
    

def ayuda_de_la_fuerza(lista, buscado):
    if usar_la_fuerza(lista, buscado) == -1:
        print(f'El objeto {buscado} no se encuentra')
    else:
        print(f'El objeto {buscado} fue encontrado!!')
        print(f'Se necesito sacar {usar_la_fuerza(lista,buscado)} elementos para obtener: {buscado}')


objeto = input('Ingrese objeto a buscar: ')
print('*************************')
ayuda_de_la_fuerza(mochila,objeto)
print('*************************')

