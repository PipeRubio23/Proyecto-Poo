from Personas import Personas

class Empleados(Personas):

    __id_empleado = 0
    __fecha_inicio = ''
    __salario = 0
    __id_estado=0
    __nom_estado=""
    Personas = Personas()

    def __init__(self):
        pass

    def getId_empleado(self):
        return self.__id_empleado
    def setId_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def getFecha_inicio(self):
        return self.__fecha_inicio
    def setFecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    
    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario = salario

    def getId_Estado(self):
        return self.__id_estado
    def setId_Estado(self, id_estado):
        self.__id_estado = id_estado

    def getNombre_Estado(self):
        return self.__nom_estado
    def setNombre_Estado(self, nom_estado):
        self.__nom_estado = nom_estado
