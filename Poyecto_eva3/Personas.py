class Personas():
    __rut = ''
    __nombres = ''
    __apellido = ''
    __edad = 0
    __direccion = ''
    __telefono = 0
    __correo = ''

    def __init__(self):
        pass

    def getRut(self):
        return self.__rut 
    def setRut(self, rut):
        self.__rut = rut

    def getNombre(self):
        return self.__nombres
    def setNombre(self, nombres):
        self.__nombres = nombres

    def getApellido(self):
        return self.__apellido
    def setApellido(self, apellido):
        self.__apellido = apellido

    def getEdad(self):
        return self.__edad
    def setEdad(self, Edad):
        self.__edad = Edad

    def getDireccion(self):
        return self.__direccion
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getCorreo(self):
        return self.__correo
    def setCorreo(self, correo):
        self.__correo = correo

    
        