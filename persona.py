class persona():
    #método constructor
    def __init__(self, numero, nombre, direccion):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion

    #creación de GETTERS
    def verNumero(self):
        return self.numero
    
    def verNombre(self):
        return self.nombre
    
    def verDireccion(self):
        return self.direccion
    
    #Creación de SETTERS
    def modificarNumero(self, nuevoNumero):
        self.numero = nuevoNumero
    
    def modificarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def modificarDireccion(self, nuevaDireccion):
        self.direccion = nuevaDireccion