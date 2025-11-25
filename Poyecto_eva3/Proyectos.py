from Empleados import Empleados

class Proyectos(Empleados):
    __id_proyecto = ''
    __titulo = ""
    __descripcion = ''
    __inicio_proyecto = ''
    __id_estado=0
    __nom_estado=""
    __id_estado = ""
    __nom_estado=""
    Empleados = Empleados()

    def __init__(self):
        pass
    
    def getId_proyecto(self):
        return self.__id_proyecto
    def setId_proyecto(self, id_proyecto):
        self.__id_proyecto = id_proyecto

    def getTitulo(self):
        return self.__titulo
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getInicio_proyecto(self):
        return self.__inicio_proyecto
    def setInicio_proyecto(self, inicio_proyecto):
        self.__inicio_proyecto = inicio_proyecto

    def getId_Estado(self):
        return self.__id_estado
    def setId_Estado(self, id_estado):
        self.__id_estado = id_estado

    def getNombre_Estado(self):
        return self.__nom_estado
    def setId_Estado(self, nom_estado):
        self.__nom_estado = nom_estado

    def getEncargado(self):
        return self.encargado
    def setEncargado(self, encargado):
        self.encargado = encargado
    
    def getId_Estado(self):
        return self.__id_estado
    def setId_Estado(self, id_estado):
        self.__id_estado = id_estado

    def getNombre_Estado(self):
        return self.__nom_estado
    def setNombre_Estado(self, nom_estado):
        self.__nom_estado = nom_estado