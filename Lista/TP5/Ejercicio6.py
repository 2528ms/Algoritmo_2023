"""
Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.
"""
import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Lista') 
from listaClass import Lista

#Se crea clase superheroes
class Superheroe():

    def __init__(self, nombre, anio_aparicion, casa_comic, bibliografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.bibliografia = bibliografia

    def __str__(self):
        return f'{self.nombre} - {self.anio_aparicion} - {self.casa_comic} - {self.bibliografia}'
    
#Se instancia la clase superheroes con sus respectivos atributos
superheroe1 = Superheroe('Thor', 1962, 'Marvel', 'martillo')
superheroe2 = Superheroe('Linterna Verde', 1940, 'DC', 'anillo')
superheroe3 = Superheroe('Wolverine', 1974, 'Marvel', 'armadura')
superheroe4 = Superheroe('Superman', 1938, 'DC', 'capa')
superheroe5 = Superheroe('Dr. Strange', 1963, 'DC', 'adsadsdsa')
superheroe6 = Superheroe('Hulk', 1962, 'Marvel', 'verde')
superheroe7 = Superheroe('Capitana Marvel', 1968, 'Marvel', 'traje')
superheroe8 = Superheroe('Batman', 1939, 'DC', 'adsadsdsa')
superheroe9 = Superheroe('Mujer Maravilla', 1941, 'DC', 'traje')
superheroe10 = Superheroe('Flash', 1940, 'DC', 'adsadsdsa')
superheroe11 = Superheroe('Star-Lord', 1976, 'Marvel', 'adsadsdsa')
superheroe12 = Superheroe('Aquaman', 1941, 'DC', 'adsadsdsa')

#Creamos lista
lista_superheroes = Lista()

#Cargamos todas las instancias de superheroes a la lista creada, a medida que lo insertamos en la lista indicamos que los ordene por nombre
for i in range(1,13):
    value = eval('superheroe' + str(i))
    lista_superheroes.insert(value,"nombre")

 
print('*********** Lista original ***********')
lista_superheroes.barrido()

print('*** Punto A - se elimina todos los datos de Linterna Verde ***')
lista_superheroes.delete('Linterna Verde','nombre')
lista_superheroes.barrido()

print('*** Punto B - el año de aparición de Wolverine ***')
buscado = lista_superheroes.get_element_by_value('Wolverine','nombre')
print( buscado.__dict__['anio_aparicion'])
 
print('*** Punto C - actualizar la casa de Dr. Strange a Marvel ***')

posicion = lista_superheroes.search('Dr. Strange','nombre')
lista_superheroes.get_element_by_index(posicion).casa_comic = 'Marvel'
print(lista_superheroes.get_element_by_value('Dr. Strange','nombre'))

print('*** Punto D - superhéroes que en su biografía menciona la palabra traje o armadura***')
for i in range(0,lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.__dict__['bibliografia'] in ['traje', 'armadura']:
        print(value)

print('*** Punto E - superhéroes cuya fecha de aparición sea anterior a 1963***')
for i in range(0,lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.__dict__['anio_aparicion'] < 1963:
        print(value.__dict__['nombre'] +' - '+value.__dict__['casa_comic'])

print('*** Punto F - Casa a la que pertenece Capitana Marvel y Mujer Maravilla***')
buscado1= lista_superheroes.get_element_by_value('Capitana Marvel', 'nombre')
print(buscado1.__dict__['nombre'] +' - '+buscado1.__dict__['casa_comic'])
buscado2= lista_superheroes.get_element_by_value('Mujer Maravilla', 'nombre')
print(buscado2.__dict__['nombre'] +' - '+buscado2.__dict__['casa_comic'])

print('*** Punto G - mostrar toda la información de Flash y Star-Lord***')
print(lista_superheroes.get_element_by_value('Flash', 'nombre'))
print(lista_superheroes.get_element_by_value('Star-Lord', 'nombre'))

print('*** Punto H - listar los superhéroes que comienzan con la letra B, M y S***')
for i in range(0,lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.__dict__['nombre'][0] in ['B', 'M' , 'S']:
        print(value.__dict__['nombre'])

print('*** Punto I - determinar cuántos superhéroes hay de cada casa de comic***')
cantMarvel= 0
cantDC= 0
for i in range(0,lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.__dict__['casa_comic'] == 'Marvel':
        cantMarvel +=1
    else:
        cantDC += 1

print(f'Marvel tiene {cantMarvel} superheroes y DC {cantDC} superheroes')
