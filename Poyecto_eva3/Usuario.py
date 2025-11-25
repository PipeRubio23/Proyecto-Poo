from Empleados import Empleados
from Proyectos import Proyectos

class Usuario(Proyectos , Empleados):
    __id_perfil = ''
    __nombre_perfil = ''
    __contraseña = ''
    Empleados = Empleados()
    Proyectos = Proyectos()

    def __init__(self):
        pass

    def getId_perfil(self):
        return self.__id_perfil
    def setId_perfil(self, id_perfil):
        self.__id_perfil = id_perfil

    def getNombre_perfil(self):
        return self.__nombre_perfil
    def setNombre_perfil(self, nombre_perfil):
        self.__nombre_perfil = nombre_perfil
    
    def getContraseña(self):
        return self.__contraseña
    def setContraseña(self, contraseña):
        self.__contraseña = contraseña