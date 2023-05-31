# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

#Import file since other folder
import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Pila') #add path the folder
import pilaClass #select file that contain of folder added
sys.path.append('/home/ms/Algoritmo_2023_MS/Cola')
import colaClass 

notificaciones = colaClass.Cola()
pilaNotificaciones = pilaClass.Pila()

apps = [{'hora':'15:00','app':'Facebook','msj':'nueva solicitud de amistad de Python'},
         {'hora':'09:15','app':'Gmail','msj':'2 mail en la bandeja de entrada'},
         {'hora':'11:32','app':'Twitter','msj':'Python a publicado un nuevo twitter'},
         {'hora':'20:48','app':'Instagram','msj':'JavaScript ha realizado un nuevo contenido'},
         {'hora':'12:18','app':'WhatsApp','msj':'nuevo mensaje de Python'},
         {'hora':'16:00','app':'LinkedIn','msj':'3 personas han visto tu perfil'},
         {'hora':'10:50','app':'Twitter','msj':'A java le ha gustado tu publicacion'},
         {'hora':'22:34','app':'Facebook','msj':' Python ha aniadido una publicacion'},   
         {'hora':'17:00','app':'Twitter','msj':'tienes un mensaje de Python'},
         {'hora':'11:46','app':'Instagram','msj':'java ha subido una nueva historia'}]


for i in range(0,len(apps)):
    notificaciones.arrive(apps[i])
    

for i in range(1,len(apps)):
  if notificaciones.on_front()['app'] == 'Facebook':
    notificaciones.atention()

for i in range(1,notificaciones.size()):
  if notificaciones.on_front()['app'] == 'Twitter' and notificaciones.on_front()['msj'].find('Python') != -1:
    print(notificaciones.on_front())
  notificaciones.move_to_end()

for i in range(1,notificaciones.size()):
  if notificaciones.on_front()['hora'] > '11:43' and notificaciones.on_front()['hora'] < '15:57':
    pilaNotificaciones.push(notificaciones.on_front())
   
  notificaciones.move_to_end()

print('*****Pila de notificaciones entre las 11:43 y 15:57 ************')
print(pilaNotificaciones.size())
while pilaNotificaciones.size() > 0:
   print(pilaNotificaciones.pop())


