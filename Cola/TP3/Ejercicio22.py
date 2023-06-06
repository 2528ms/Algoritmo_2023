# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

#Import file since other folder
import sys #Import library 'sys'
#import pilaClass #select file that contain of folder added
sys.path.append('/home/ms/Algoritmo_2023_MS/Cola')
import colaClass 

personajesMarvel = colaClass.Cola()

personajes = [['Tnoy Stark', 'Iron Man', 'M'], 
              ['Brie Larson', 'Capitana Marvel', 'F'],
              ['Steve Rogers', 'Capitán América', 'M'], 
              ['Natasha Romanoff', 'Black Widow', 'F'],
              ['Paul Rudden', 'Scott Lang', 'M'],
              ['Tom Holland', 'Spider-Man', 'M'],
              ['Carol Danvers','Binary', 'F']              
              ]


for value in personajes:
    dic = {}
    dic['personaje'] = value[0]
    dic['superheroe'] = value[1]
    dic['genero'] = value[2]
    personajesMarvel.arrive(dic)


for i in range(0,personajesMarvel.size()):
    if personajesMarvel.on_front()['superheroe'] == 'Capitana Marvel':
        print('El nombre de la personaje Capitana Marvel es: '+personajesMarvel.on_front()['personaje']) #Punta A
        print()
    elif personajesMarvel.on_front()['superheroe'] == 'Scott Lang':
        print('El nombre de la personaje Scott Lang es: '+personajesMarvel.on_front()['personaje']) #Punto D
        print()
    elif personajesMarvel.on_front()['personaje'] == 'Carol Danvers':
        print('El nombre de superhereo del personaje Carol Danvers es: '+personajesMarvel.on_front()['superheroe']) #Punto F
        print()
    personajesMarvel.move_to_end()


for i in range(0,personajesMarvel.size()):
    if personajesMarvel.on_front()['genero'] == 'F': #Punta B
        print('superhéroes femenino: '+ personajesMarvel.on_front()['superheroe'])
    else:
        print('Personaje Mascualino: '+ personajesMarvel.on_front()['personaje']) #Punto C
    personajesMarvel.move_to_end()

print()
for i in range(0,personajesMarvel.size()):
    if personajesMarvel.on_front()['personaje'][0] == 'S' or personajesMarvel.on_front()['superheroe'][0] == 'S': #Punto E
        print('superhéroes o personaje cuyos nombres comienzan con la letra S -> '+
              personajesMarvel.on_front()['personaje']+', '+personajesMarvel.on_front()['superheroe'])
    personajesMarvel.move_to_end()

