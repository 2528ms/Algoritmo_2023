class Personaje():

    def __init__(self, superheroe, nombre, grupo, anio_aparicion):
        self.superheroe = superheroe
        self.nombre = nombre
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion

    def __str__(self):
        return f'{self.superheroe } - {self.nombre} - {self.grupo} - {self.anio_aparicion}'
    
personaje1 = Personaje('Iron Man', 'Tony Stark', 'Avengers', 1953)
personaje2 = Personaje('Captain America', 'Steve Rogers', 'Avengers', 1941)
personaje3 = Personaje('Thor', 'Thor Odinson', 'Avengers', 1962)
personaje4 = Personaje('Vlack Widow', 'Natasha Romanoff', 'Avengers', 1954)
personaje5 = Personaje('Hawkeye', 'Clint Barton', 'Avengers', 1964)
personaje6 = Personaje('Star-Lord', 'Peter Quill', 'Guardianes de la Galaxia', 1976)
personaje7 = Personaje('Spider-Man', ' Peter Parker', 'Avengers', 1962)
personaje8 = Personaje('Black Panther', ' TChalla', 'Avengers', 1956)
personaje9 = Personaje('Capitana Marvel', 'Carol Danvers', 'Avengers', 1968)
personaje10 = Personaje('Falcon', ' Sam Wilson', 'Avengers', 1969)
personaje11 = Personaje('Quicksilver', ' Pietro Maximoff', 'Avengers', 1954)
personaje12 = Personaje('Vision', ' Vision', 'Avengers', 1968)
personaje13 = Personaje('Ant-Man', ' Scott Lang', 'Avengers', 1979)
personaje14 = Personaje('Man', ' Stark', 'Avengers', 1963)
personaje15 = Personaje('Gamora  ', ' Gamora  ', ' Guardianes de la Galaxia', 1975)
personaje16 = Personaje('War Machine ', ' James Rhodes ', 'Avengers', 1979)

personajes =[personaje1,personaje2,personaje3,personaje4,personaje5,personaje6,personaje7,personaje8,personaje9,personaje10,
             personaje11,personaje12,personaje13,personaje14,personaje15,personaje16]

personaje_aux1 = Personaje('Hulk ', ' Bruce Banner ', 'Avengers', 1955)
personaje_aux2 = Personaje('Rocket Raccoon ', ' Rocket ', 'Guardianes de la Galaxia', 1976)
personaje_aux3 = Personaje('Loki ', ' Loki ', 'Los cuatro fantasticos', 1949)
personaje_aux4 = Personaje('Nebula ', ' Nebula ', 'Guardianes de la Galaxia', 1985)

personajes_aux = [personaje_aux1,personaje_aux2,personaje_aux3, personaje_aux4]

from listaClass import Lista
from colaClass import Cola
from pilaClass import Pila

listaPersonajes = Lista()
guardianesDeLaGalaxia = Cola()
superheroesDesc = Pila()

#Carga de elementos a la lista
for personaje in personajes:
    listaPersonajes.insert(personaje,"superheroe")

#Dada una lista auxiliar agregarlos a la lista
for personaje in personajes_aux:
    listaPersonajes.insert(personaje,"superheroe")

print('********A. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje******')
buscado = False
for i in range(0,listaPersonajes.size()):
    if listaPersonajes.get_element_by_index(i).superheroe == "Capitana Marvel":
        print('El nombre de Capitana Marvel es: ', listaPersonajes.get_element_by_index(i).nombre)
        buscado = True

if not buscado:
    print('El superheroe Capitana Marvel no se encuentra en la lista')

print('********B. La cantidad de superheroes que pertenezcan al grupo “Guardianes de la galaxia” son******')
for i in range(0,listaPersonajes.size()):
    if listaPersonajes.get_element_by_index(i).grupo == "Guardianes de la Galaxia":
        guardianesDeLaGalaxia.arrive(listaPersonajes.get_element_by_index(i))

print('Cantidad de superheroes que pertenezcan al grupo “Guardianes de la galaxia”: ',guardianesDeLaGalaxia.size())

print('*******C. Listar superheroes que pertenecen al grupo “Los cuatro fantasticos” y “Guardoanes de la galaxia”*******')
for i in range(0,listaPersonajes.size()):
    if listaPersonajes.get_element_by_index(i).grupo == "Guardianes de la Galaxia" or listaPersonajes.get_element_by_index(i).grupo == "Los cuatro fantasticos" :
        superheroesDesc.push(listaPersonajes.get_element_by_index(i))

while superheroesDesc.size() > 0:
    print(superheroesDesc.pop())

print('*******D. Listar superheroes que cuyo año de aparición sea posterior a 1960*******')
for i in range(0,listaPersonajes.size()):
    if listaPersonajes.get_element_by_index(i).anio_aparicion > 1960:
        print(listaPersonajes.get_element_by_index(i).superheroe +', anio '+str(listaPersonajes.get_element_by_index(i).anio_aparicion))

#*******E. Modificar superhereo mal cargado*******
listaPersonajes.set_value('Vlack Widow','Black Widow',"nombre")

print('********G. Mostrar todos los personajes que comienzan con C, P o S.******')
for i in range(0,listaPersonajes.size()):
    if listaPersonajes.get_element_by_index(i).superheroe[0] in ['C','P','S']:
        print(listaPersonajes.get_element_by_index(i).superheroe)

