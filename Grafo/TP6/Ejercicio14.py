# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el smart Tv.

from grafo import Grafo
from random import randint

ambientes = [
    ['cocina', ['comedor', 'cochera', 'quincho', 'sala de estar', 'patio']],
    ['comedor', ['cochera', 'quincho', 'baño 1']],
    ['cochera', ['quincho', 'baño 1', 'baño 2']],
    ['quincho', ['comedor', 'baño 2', 'habitación 1']],
    ['baño 1', ['terraza', 'habitación 1', 'habitación 2']],
    ['baño 2', ['habitación 1', 'habitación 2', 'sala de estar']],
    ['habitacion 1', ['habitación 2', 'sala de estar', 'terraza']],
    ['habitacion 2', ['sala de estar', 'terraza', 'patio']],
    ['sala de estar', ['terraza', 'patio', 'cocina', 'baño 1','habitación 2']],
    ['terraza', ['patio', 'cocina', 'comedor']],
    ['patio', ['cocina', 'comedor', 'cochera']]
]

home = Grafo(dirigido=False)

#Punto A cargamos los vertices (cada ambiente es un vertice)
for ambiente in ambientes:
    home.insert_vertice(ambiente[0])

#DATO: No podemos insertar los vertices y las aristas al mismo tiempo, ya que las insertar las aristas 
# deben existir el origen y el destino(los vertices) 

#Punto B cargamos las aristas a cada vertice 
for ambiente in ambientes:
    origen = ambiente[0]
    adyacentes = ambiente[1]
    for destino in adyacentes:
        metros = randint(1,15)
        home.insert_arist(origen,destino,metros)
print('**** DATOS DEL GRAFO - PUNTO A y B ****')
home.barrido()

print('**** PUNTO C *****')
arbol_expansion_min = home.kruskal()
total_metos = 0
print(f'El arbol rbol de expansion min del grafo es: {arbol_expansion_min}')
print()
print('cada nodo del arbol es:')
for arbol in arbol_expansion_min:
    for nodo in arbol.split(';'):
        #print(nodo) #formato del nodo [origen-destino-peso]
        datos = nodo.split('-')
        print(datos)
        total_metos = total_metos + int(datos[2])
print()
print(f'El todal de metros de cable para conectar todos los ambientes es {total_metos} mts')
print()


print('**** PUNTO D *****')
origen = 'habitacion 1'
destino = 'sala de estar'
pos_origen = home.search_vertice(origen, criterio='nombre')
pos_destino = home.search_vertice(destino, criterio='nombre')
camino_mas_corto = None
total_metros = 0
if(pos_origen is not None and pos_destino is not None):
    if(home.has_path(origen, destino, criterio='nombre') is not None):
        camino_mas_corto = home.dijkstra(origen, destino)
        print('nodos del camino mas corto:')    
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop() #value es un tupla que contine [vertice destino - peso - vertice origen]
            if destino == value[0]:
                total_metros = value[1]
            print(value[0],value[1], value[2])
    print()
    print(f'La cantidad de metros de clabe de red para conectar {origen} con {destino} son: {total_metros} mts')
