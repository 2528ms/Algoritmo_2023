# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos 
# personajes que se relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes y quienes son 
# d) cargue al menos los siguientes personajes: Luke skywalter, Darth Vader, Yoda, Boba Feet, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8

from grafo import Grafo
from random import randint
grafo_personajes = Grafo(dirigido=False)

#Punto D
personajes_star_wars = ['Luke skywalter', 'Darth Vader', 'Yoda', 'Boba Feet', 'C-3PO', 'Leia', 'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8']

#Punto A 
for personaje in personajes_star_wars:
    grafo_personajes.insert_vertice(personaje)
    capitulo = randint(1,12)
    grafo_personajes.insert_arist(personaje, personajes_star_wars[capitulo-1], capitulo)


grafo_personajes.barrido()
print()

#Punto B
arbol_expansion_min = grafo_personajes.kruskal() 
if 'Yoda' in arbol_expansion_min:
    print('Si contiene Yoda')
else:
    print('No contiene Yoda')
print(arbol_expansion_min)

#Punto C
print()
max_peso = 0
personajes = None

#Recorremos el grafo entero
for i in range(grafo_personajes.size()):
    vertice = grafo_personajes.get_element_by_index(i) #obtenemos cada vertice del grado
    for arista in range(vertice[1].size()): #recorremos todas las aristas de cada vertice
        arista_actual = vertice[1].get_element_by_index(arista) #vamos almanecando el peso (cant de episodios)
        if arista_actual.peso > max_peso:
            max_peso = arista_actual.peso
            personajes = (vertice[0], arista_actual.vertice)

print(f"El numero max de episodios compartidos es {max_peso}, entre {personajes[0]} y {personajes[1]}")



