import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Pila') 
import pilaClass #select file that contain of folder added

peliculas = [{'pelicula':'Iron Man ','productora':'Marvel Studios', 'estreno': 2008},
             {'pelicula':'Transformers','productora':'PARAMOUNT PICTURES', 'estreno': 2014},
             {'pelicula':'El robo del siglo','productora':'Cine argentino', 'estreno': 2020},
             {'pelicula':'Capitán America: Civil War ','productora':'Marvel Studios', 'estreno': 2016},
             {'pelicula':'Noche de juegos','productora':'WARNER BROS', 'estreno': 2018},
             {'pelicula':'El vuelo (Flight)','productora':'PARAMOUNT PICTURES', 'estreno': 2012},
             {'pelicula':'Capitán America: El soldado de invierno ','productora':'Marvel Studios', 'estreno': 2014},
             {'pelicula':'El hombre de acero','productora':'WARNER BROS', 'estreno': 2016},
             {'pelicula':'Doctor Extraño ','productora':'Marvel Studios', 'estreno': 2016}
            ]

stack = pilaClass.Pila()
stack_aux = pilaClass.Pila()

for i in range(0,len(peliculas)):
    stack.push(peliculas[i])

cantEstrenos = 0

while stack.size() > 0:
    element = stack.pop()
    stack_aux.push(element)
    if (element['estreno'] == 2014):
        print('A) Pelicula estrenada en el año 2014 => ' + element['pelicula'])
    elif (element['estreno'] == 2018):
        cantEstrenos += 1
    

print(f'B) La cantidad de peliculas estrenadas en el año 2018 son: {cantEstrenos}')

while stack_aux.size() > 0:
    element = stack_aux.pop()
    stack.push(element)
    if(element['productora'] == 'Marvel Studios' and element['estreno'] == 2016):
        print('C) '+element['pelicula']+' Pelicula producida por Marvel Studio en el año 2016')
    

