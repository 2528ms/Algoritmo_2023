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
        
# home.barrido()
#Punto C
# arbol_expancion_min = home.kruskal()
# print(arbol_expancion_min)

#Punto D
origen = 'habitacion 1'
destino = 'sala de estar'
pos_origen = home.search_vertice(origen, criterio='nombre')
pos_destino = home.search_vertice(destino, criterio='nombre')
camino_mas_corto = None
total_metros = 0
if(pos_origen is not None and pos_destino is not None):
    if(home.has_path(origen, destino, criterio='nombre') is not None):
        camino_mas_corto = home.dijkstra(origen, destino)
        fin = destino
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            # print(value[0])
            if fin != value[0]:
                index = home.search_vertice(value[0], criterio='nombre')
                vertice = home.get_element_by_index(index)
                #print(vertice[1])
                for index in range(vertice[1].size()):
                    aristas = vertice[1].get_element_by_index(index)
                    total_metros= total_metros + aristas.peso
                    
    print(f'La cantidad de metros de clabe de red para conectar {origen} con {destino} son: {total_metros} mts')
            



    