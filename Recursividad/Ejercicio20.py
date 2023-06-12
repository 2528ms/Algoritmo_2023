# Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
# manera recursiva, y permita determinar si un valor dado está o no en dicha lista.

def busqueda_secuencial(lista, buscado):
    if len(lista) == 0:
        return -1
    elif lista[-1] == buscado:
        return len(lista)-1
    else:
        return busqueda_secuencial(lista[0:-1], buscado)



lista_valores = [1, 4, 7, 10, 12]

print(busqueda_secuencial(lista_valores, 4))