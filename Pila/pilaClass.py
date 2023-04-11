

class Pila():
    """Stack class"""

    def __init__(self): #Constructor de la clase
        self.__elements = [] #self = this en otros lenguajes

    def push(self, dato): #push agregar elemento
        self.__elements.append(dato) #appen agrega un elemento al final (cima de la pila)

    def pop(self):         #pop quitar elemento
        if self.size() > 0:
            dato = self.__elements.pop() #pop quita el ultimo elemento de la cima
            return dato

    def size(self):
        return len(self.__elements) #tamaño de la pila

    def on_top(self): #retorna el elemento que esta en la cima
        if self.size() > 0:
            return self.__elements[-1]

