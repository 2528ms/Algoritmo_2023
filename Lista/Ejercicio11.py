
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
personaje4 = Personaje('Darth Vader',203, 45,'Masculino','Humano','Tatooine',['III', 'IV', 'V', 'VI'])
personaje5 = Personaje('Obi-Wan Kenobi',182, 57,'Masculino','Humano','Stewjon',['I', 'II', 'III', 'IV', 'V', 'VI'])
personaje6 = Personaje('Rey',170, 19,'Femenino','Humano','Jakku',['VII', 'VIII', 'IX'])
personaje7 = Personaje('Finn',178, 23,'Masculino','Humano','Desconocido',['VII', 'VIII', 'IX'])
personaje8 = Personaje('Chewbacca',228, 200,'Masculino','Wookiee','Kashyyyk',['III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'])
personaje9 = Personaje('Emperor Palpatine',170, 86,'Masculino','Humano','Naboo',['I', 'II', 'III', 'VI', 'IX'])
personaje10 = Personaje('Padmé Amidala',165, 14,'Femenino','Humano','Naboo',['I', 'II', 'III'])
personaje11 = Personaje('Anakin Skywalker',188, 9,'Masculino','Humano','Tatooine',['I', 'II', 'III','VI'])
personaje12 = Personaje('Mace Windu',188, 0,'Masculino','Humano','Haruun Kal',['I', 'II', 'III'])
personaje13 = Personaje('Kylo Ren',189, 29,'Masculino','Humano','Desconocido',['VII', 'VIII', 'IX'])
personaje14 = Personaje('Jyn Erso',170, 22,'Masculino','Humano','Vallt',['IV', 'V' , 'VI'])
personaje15 = Personaje('Droideka',190, 80,'Desconocido','Droide','Alderaan',['I', 'II', 'III'])
personaje16 = Personaje('BB-8',67, 80,'Desconocido','Droide','Desconocido',[ 'VII', 'VIII', 'IX'])
personaje17 = Personaje('Yoda',66, 0,'Masculino','Desconocida','Desconocida',['II', 'III', 'V', 'VI', 'VIII'])

#Creamos lista
lista_personajes = Lista()

#Cargamos todas las instancias de personaje a la lista creada, a medida que lo insertamos en la lista indicamos que los ordene por nombre
for i in range(1,18):
    value = eval('personaje' + str(i))
    lista_personajes.insert(value,"nombre")


print('*********** Lista original ***********')
lista_personajes.barrido()
print()
print('*** Punto A - listar todos los personajes de género femenino ***')
# for i in range(0,lista_personajes.size()):
#     value = lista_personajes.get_element_by_index(i)
#     if value.__dict__['genero'] == 'Femenino':
#         print(value)
# print()
for i in range(0,lista_personajes.size()):
    value = lista_personajes.get_element_by_index(i)
    if  value.genero == 'Femenino':
        print(value)
print()

print('*** Punto B - personajes de especie Droide que aparecieron en los primeros 6 episodios***')
for i in range(0,lista_personajes.size()):
    cont_episodios = 0
    value = lista_personajes.get_element_by_index(i)
    if value.__dict__['especie'] == 'Droide':
        for i in range(0,len(value.__dict__['episodios'])):
            if value.__dict__['episodios'][i] < 'VI':
                    cont_episodios +=1
    
    if len(value.__dict__['episodios']) == cont_episodios:
         print(value)
print()        
                     
print('*** Punto C - mostrar toda la información de Darth Vader y Han Solo***')
print(lista_personajes.get_element_by_value('Darth Vader','nombre'))
print(lista_personajes.get_element_by_value('Han Solo','nombre'))
print()
print('*** Punto D - listar los personajes que aparecen en el episodio VII y en los tres anteriores***')
for i in range(0,lista_personajes.size()):
    value = lista_personajes.get_element_by_index(i)
    if  value.episodios == ['IV','V','VI','VII']:
        print(value)
print()
print('*** Punto E - mostrar los personajes con edad mayor a 40 años y de ellos el mayor***')
lista_personajes.order_by('edad', True)

for i in range(0,lista_personajes.size()):
    value = lista_personajes.get_element_by_index(i)
    if value.__dict__['edad'] > 40:
         print(str(value.__dict__['nombre']) + ' - ' +str(value.__dict__['edad'])+' anios')

mayor =  lista_personajes.get_element_by_index(0)   
print('El personaje de mayor edad es : ' +  str(mayor.__dict__['nombre']))
print()
print('*** Punto F - eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI***')
for i in range(0,lista_personajes.size()):
    value = lista_personajes.get_element_by_index(i)
    if  value.episodios == ['IV','V','VI']:
        print(value)
print()
print('*** Punto G - listar los personajes de especie humana cuyo planeta de origen es Alderaan***')
for i in range(0,lista_personajes.size()):
    value = lista_personajes.get_element_by_index(i)
    if value.__dict__['especie'] == 'Humano' and value.__dict__['planeta'] == 'Alderaan':
         print(str(value.__dict__['nombre']) + ' - especie: ' +str(value.__dict__['especie'])+' - planeta: ' +str(value.__dict__['planeta']))

print()
print('*** Punto H - mostrar toda la información de los personajes cuya altura es menor a 70 centímetros***')
for i in range(0,lista_personajes.size()):
    value = lista_personajes.get_element_by_index(i)
    if value.__dict__['altura'] < 70:
         print(str(value.__dict__))
print()
print('*** Punto I - determinar en qué episodios aparece Chewbacca y mostrar además toda su información***')
index = lista_personajes.search('Chewbacca','nombre')
print('Chewbacca aparece en los episodios ' + str(lista_personajes.get_element_by_index(index).episodios))
print(lista_personajes.get_element_by_index(index).__dict__)