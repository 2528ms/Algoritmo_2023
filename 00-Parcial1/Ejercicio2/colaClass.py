class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):         #Agrega un nuevo elemento en el final de la cola
        self.__elementos.append(value) 

    def atention(self):             #elimina el primer elemento de la cola
        if self.size() > 0:
            return self.__elementos.pop(0) 

    def size(self):                 #devuelve el tamaño de la cola
        return len(self.__elementos) 

    def on_front(self):             #devuelve el valor del primer elemento de la cola
        if self.size() > 0:
            return self.__elementos[0] 

    def move_to_end(self):          #Mueve el primer elemento al ultimo lugar de la cola
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux