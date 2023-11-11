# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, 
# para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

from grafo import Grafo
from random import randint
from listado_maravillas import Maravillas

#Punto F
maravillas = Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo, distancia):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
        self.distancia = distancia
    
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}-{self.distancia}'


#Creamos los vertices del grado 
for maravilla in Maravillas: #Recorremos la lista con las maravillas
    maravillas.insert_vertice(Maravilla(maravilla["Nombre"], maravilla["Pais"], maravilla["Tipo"], maravilla["Distancias"]), criterio='nombre')
    #Insertamos como Vertice cada Maravillas con todos sus datos

# Crear aristas entre los vertices del grafo
for i in range(maravillas.size() - 1):  # Restamos 1 para evitar index fuera de rango
    # Obtenemos las instancias de las maravillas consecutivas insertadas al grafo como vertice
    origen = maravillas.get_element_by_index(i)[0].nombre
    destino = maravillas.get_element_by_index(i + 1)[0].nombre
    km = randint(1000, 2000) #El peso de la arista hace referencia a los kilometros entre ambas maravillas
    maravillas.insert_arist(origen, destino, km, criterio_vertice='nombre')



print()
maravillas.barrido()

#PUNTO C
#aem= Arbol de expansion minima
aem_arquitectonicas = maravillas.kruskal_por_tipo("arquitectonica")
aem_naturales = maravillas.kruskal_por_tipo("natural")

print('El arbol de expansion min del grafo es para las Maravillas arquitectonicas es: ')
print(aem_arquitectonicas)
print()
print('cada nodo del arbol es:')
for nodo in aem_arquitectonicas:
    datos = nodo.split(';') #formato del nodo [origen-destino; peso ; tipo]
    print(f'{datos[0]} - {datos[1]} km') 

print()
print('El arbol de expansion min del grafo es para las Maravillas naturales es: ')
print(aem_naturales)
print()
print('cada nodo del arbol es:')
for nodo in aem_naturales:
    datos = nodo.split(';') #formato del nodo [origen-destino; peso ; tipo]
    print(f'{datos[0]} - {datos[1]} km') 

print()
#PUNTO D y E s arman las listas de paises por tipo de maravilla
naturales_por_pais = []
arquitectonicas_por_pais = []

for i in range(maravillas.size()):  
    paises = maravillas.get_element_by_index(i)[0].pais
    tipo = maravillas.get_element_by_index(i)[0].tipo
    for pais in paises:
        if tipo == 'natural':
            naturales_por_pais.append(pais)
        else:
            arquitectonicas_por_pais.append(pais)

#PUNTO D
existe = False
for pais in naturales_por_pais:
    if pais in arquitectonicas_por_pais:
        existe = True
        print(f'El {pais} tiene maravillas arquitectónicas y naturales')

if not existe:
    print(f'Ningun Pais tiene ambas maravillas, arquitectónicas y naturales')

print()
#PUNTO E

def contar_in_lista(lista, aux):
    frecuencia = {} #definimos un diccionario
    for elemento in lista:
        #insertamos cada elemento al diccionario, con la clave "elemento"
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
        #la funcion get() se fija si el elemento existe en el dic le suma 1, si no le asigna 0 al valor asociado a la clave
        #formato de del dic {"elemento": valor}

    #Recorrer cada item del dic 
    for elemento, count in frecuencia.items():
        if count > 1:
            return f"{elemento} tiene {count} maravillas {aux}."
        
    return f"Ningun pais tiene mas de una Maravilla {aux}"

print(contar_in_lista(naturales_por_pais,"naturales"))
print(contar_in_lista(arquitectonicas_por_pais,"arquitectonicas"))