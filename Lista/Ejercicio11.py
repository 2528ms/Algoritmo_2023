
from listaClass import Lista

#Se crea clase Personaje
class Personaje():

    def __init__(self, nombre, altura, edad, genero, especie, planeta, episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodios = episodios

    def __str__(self):
        return f'{self.nombre} - {self.altura} - {self.edad} - {self.genero} - {self.especie} - {self.planeta} - {self.episodios}'

personaje1 = Personaje('Luke Skywalker',172, 19,'Masculino','Humano','Tatooine',['IV', 'V', 'VI', 'VII', 'VIII', 'IX'])
personaje2 = Personaje('Leia Organa',150, 19,'Femenino','Humano','Alderaan',['IV', 'V', 'VI', 'VII', 'VIII', 'IX'])
personaje3 = Personaje('Han Solo',180, 29,'Masculino','Humano','Corellia',['IV', 'V', 'VI', 'VII'])
personaje4 = Personaje('Yoda',66, 'Desconocida','Masculino','Desconocida','Desconocida',['II', 'III', 'V', 'VI', 'VIII'])
personaje4 = Personaje('Darth Vader',203, 45,'Masculino','Humano','Tatooine',['III', 'IV', 'V', 'VI'])
personaje5 = Personaje('Obi-Wan Kenobi',182, 57,'Masculino','Humano','Stewjon',['I', 'II', 'III', 'IV', 'V', 'VI'])
personaje6 = Personaje('Rey',170, 19,'Femenino','Humano','Jakku',['VII', 'VIII', 'IX'])
personaje7 = Personaje('Finn',178, 23,'Masculino','Humano','Desconocido',['VII', 'VIII', 'IX'])
personaje8 = Personaje('Chewbacca',228, 200,'Masculino','Wookiee','Kashyyyk',['III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'])
personaje9 = Personaje('Emperor Palpatine',170, 86,'Masculino','Humano','Naboo',['I', 'II', 'III', 'VI', 'IX'])
personaje10 = Personaje('Padmé Amidala',165, 14,'Femenino','Humano','Naboo',['I', 'II', 'III'])
personaje11 = Personaje('Anakin Skywalker',188, 9,'Masculino','Humano','Tatooine',['I', 'II', 'III','VI'])
personaje12 = Personaje('Mace Windu',188, 'Desconocida','Masculino','Humano','Haruun Kal',['I', 'II', 'III'])
personaje13 = Personaje('Kylo Ren',189, 29,'Masculino','Humano','Desconocido',['VII', 'VIII', 'IX'])
personaje14 = Personaje('Jyn Erso',170, 22,'Masculino','Humano','Vallt',['I'])
personaje15 = Personaje('Droideka',190, 80,'Desconocido','Droide','Desconocido',['I', 'II', 'III'])
personaje16 = Personaje('BB-8',67, 80,'Desconocido','Droide','Desconocido',[ 'VII', 'VIII', 'IX'])

#Creamos lista
lista_personajes = Lista()

#Cargamos todas las instancias de personaje a la lista creada, a medida que lo insertamos en la lista indicamos que los ordene por nombre
for i in range(1,17):
    value = eval('personaje' + str(i))
    lista_personajes.insert(value,"nombre")


print('*********** Lista original ***********')
lista_personajes.barrido()
print()
# print('*** Punto A - listar todos los personajes de género femenino ***')
# for i in range(0,lista_personajes.size()):
#     value = lista_personajes.get_element_by_index(i)
#     if value.__dict__['genero'] == 'Femenino':
#         print(value)

# print('*** Punto B - personajes de especie Droide que aparecieron en los primeros 6 episodios***')

# for i in range(0,lista_personajes.size()):
#     cont_episodios = 0
#     value = lista_personajes.get_element_by_index(i)
#     if value.__dict__['especie'] == 'Droide':
#         for i in range(0,len(value.__dict__['episodios'])):
#             if value.__dict__['episodios'][i] < 'VI':
#                     cont_episodios +=1
    
#     if len(value.__dict__['episodios']) == cont_episodios:
#          print(value)
        
                     
print('*** Punto C - mostrar toda la información de Darth Vader y Han Solo***')
print(lista_personajes.get_element_by_value('Darth Vader','nombre'))
print(lista_personajes.get_element_by_value('Han Solo','nombre'))

print('*** Punto C - listar los personajes que aparecen en el episodio VII y en los tres anteriores***')
#REALIZAR!!!!!!