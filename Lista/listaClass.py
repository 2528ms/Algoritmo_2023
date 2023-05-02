class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value):
        if len(self.__elements) == 0:
            self.__elements.append(value)
        elif value < self.__elements[0]:
            self.__elements.insert(0, value)
        elif value >= self.__elements[-1]:
            self.__elements.append(value)
        else:
            index = 1
            while value >= self.__elements[index]:
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value):
        position = None
        for index, value in enumerate(self.__elements):
            if search_value == value:
                position = index
                break
        return position

    def delete(self, value):
        return_value = None
        pos = self.search(value)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def get_element_by_value(self, value):
        return_value = None
        pos = self.search(value)
        
        if pos is not None:
            return_value = self.__elements[pos]
        return return_value

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value