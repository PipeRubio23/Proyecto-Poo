from Usuario import Usuario
from Empleados import Empleados
from Proyectos import Proyectos
from DAO import DAO
from beautifultable import BeautifulTable
from os import system
import os
from datetime import datetime
from cryptography.fernet import Fernet
import json
import Requests


class Funciones(Usuario):
    op = 0 
    
    usu = Usuario()
    emp = Empleados()
    pro = Proyectos()
    d = DAO()

    def __init__(self):
        pass

#-------------------------------------------------------------------------------------
#----------------------------------Inicio de Sesion-----------------------------------
#-------------------------------------------------------------------------------------
#     
    def inicio_sesion(self):
            while True:
                system("cls")
                print("------------------")
                print("Inicio de Sesion")
                print("------------------")
                
                nom = input("Ingrese nombre: ").strip().upper()
                if len(nom.strip()) < 1 or len(nom.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 20 CARACTERES")
                    system("pause")
                    continue
                nom = nom.strip()
                r = self.d.iniciosecion(nom)
                
                if r is not None:
                    break
                else:
                    print(f"ERROR, {nom} No Existe")
                    print("Intente con otra!")
                    system("pause")
            while True:
                system("cls")
                contra = input("Ingrese Contraseña: ")
                if len(contra.strip()) < 1 or len(contra.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                    continue
                else:
                    
                    clave_fernet = "3yDYUan7tufWfCBwR96QSYXkisCW-YehF6lqPZUkoQQ="
                    f = Fernet(clave_fernet)
                    contra_desencriptada = f.decrypt(r.getContraseña()).decode()
                    
                    if contra != contra_desencriptada:
                        print("ERROR: Contraseña incorrecta")
                        system("pause")
                        continue
                    elif contra_desencriptada == contra:
                        print("BIENVENIDO!!!")
                        system("pause")
                        if nom == "GERENTE":
                            self.menu()
                        elif nom == "EMPLEADO":
                            self.menu_e()
                    break
                    

#-------------------------------------------------------------------------------------
#------------------------------------Menu Inicial-------------------------------------
#-------------------------------------------------------------------------------------
    def menuMejorado(self):
        while True:
            try:
                system("cls")
                print("---------------------")
                print("-----Menu inicial----")
                print("---------------------")
                print("1- iniciar sesion")
                print("2- Salir")
                self.op = int(input("Elija una Opcion: "))

                if self.op == 1:
                    self.inicio_sesion()
                if self.op == 2:
                    print("Programa finalizado")
                    system("pause")
                    self.salir()
                else:
                    system("cls")
                    print("Error, Elija una Opcion")
                    system("pause")
                    self.menuMejorado()
            except:
                print("Error al seleccionar opcion ")
                system("pause")
                self.menuMejorado()

#-------------------------------------------------------------------------------------
#-------------------------------Menu para Empleados-----------------------------------
#-------------------------------------empleados---------------------------------------
    def menu_e(self):
            try:
                system("cls")
                print("------------------------------")
                print("--------Menu Empleados--------")
                print("------------------------------")
                print("1- Gestion Empleados")
                print("2- Gestion Proyectos")
                print("3- Cerra Cesion")
                self.op = int(input("Elija una Opcion: "))

                if self.op == 1:
                    self.menu_empleados_e()
                if self.op == 2:
                    self.menu_proyectos_e()
                if self.op == 3:
                    self.menuMejorado()
                else:
                    system("cls")
                    print("Error, Elija una Opcion")
                    system("pause")
                    self.menu_e()
            except:
                print("Error, Elija una Opcion Numerica")
                system("pause")
                self.menu_e()
                
#-------------------------------------------------------------------------------------  

    def menu_empleados_e(self):
            try:
                system("cls")
                print("-------------------------------")
                print("-------Gestion Empleados-------")
                print("-------------------------------")
                print("1- Listar Empleado")
                print("2- Buscar Empleado")
                print("3- Estadiscticas Empleado")
                print("4- Salir")
                self.op_empleados = int(input("Elija una Opcion: "))

                if self.op_empleados == 1:
                    self.listar_empleado_e()
                if self.op_empleados == 2:
                    self.buscar_empleado_e()
                if self.op_empleados == 3:
                    self.estadisticas_empleado_e()             
                if self.op_empleados == 4:
                    self.menu_e()
                else:
                    system("cls")
                    print("Error, Elija una Opcion")
                    system("pause")
                    self.menu_empleados_e()
            except:
                print("Error al elegir opcion")
                system("pause")
                self.menu_empleados_e()

#------------------------------------------------------------------------------------- 
    def listar_empleado_e(self):
            while True:
                try:
                    system("cls")
                    print("--------------------------------")
                    print("--------Listar Empleados--------")
                    print("--------------------------------")
                    print("1- Listar Todos los Empleado")
                    print("2- Listar Empleados Habilitados")
                    print("3- Listar Empleados Suspendidos")
                    print("4- Salir")
                    opl= int(input("Digite una de las Opciones: "))
                    if opl == 1:
                        system("cls")
                        print("--------------------------------")
                        print("---------Lista Empleados--------")
                        print("--------------------------------")
                        r = self.d.ListarEmpleados()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "RUT", "NOMBRE", "APELLIDO", "EDAD", "INICIO", "SALARIO", "ESTADO" ]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] ] )
                
                            print(tabla)

                            system("pause")
                            self.menu_empleados_e()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 2:
                        system("cls")
                        print("--------------------------------------------")
                        print("--------Lista Empleados Hablilitados--------")
                        print("--------------------------------------------")
                        r = self.d.ListarEmpleadosHabilitados()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "RUT", "NOMBRE", "APELLIDO", "EDAD", "INICIO", "SALARIO", "ESTADO" ]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] ] )
                
                            print(tabla)

                            system("pause")
                            self.menu_empleados_e()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 3:
                        system("cls")
                        print("--------------------------------------------")
                        print("--------Lista Empleados Suspendidos---------")
                        print("--------------------------------------------")
                        r = self.d.ListarEmpleadosSuspendidos()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "RUT", "NOMBRE", "APELLIDO", "EDAD", "INICIO", "SALARIO", "ESTADO" ]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] ] )
                
                            print(tabla)

                            system("pause")
                            self.menu_empleados_e()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 4:
                        self.menu_empleados_e()
                    else:
                        print("ERROR, ELIJA UNA DE LAS OPCIONES")
                        system("pause")
                        self.listar_empleado_e()
                except:
                    print("Error al Digitar Opcion")
                    system("pause")


    #-------------------------------------------------------------------------------------

    def buscar_empleado_e(self):
        try:
            system("cls")
            print("--------------------------------")
            print("--------Buscar Empleados--------")
            print("--------------------------------")
            self.rut = input("Ingrese rut: ")
            if len(self.rut.strip()) < 1 or len(self.rut.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                    self.menu_empleados_e()
            else:
                self.rut = self.rut.strip()
                r = self.d.buscarEmpleado(self.rut)
                if r is not None:  
                    system("cls")
                    print(f"Empleado Encontrado!!!")
                    print(f"RUT: {r.getRut()}")
                    print(f"NOMBRE: {r.getNombre()}")
                    print(f"APELLIDO: {r.getApellido()}")
                    print(f"EDAD: {r.getEdad()}")
                    print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                    print(f"SALARIO: {r.getSalario()}")
                    print(f"Estado Empleado: {r.getNombre_Estado()}")
                    system("pause")
                    self.menu_empleados_e()
                else:
                    print("Este Rut No Existe!!!")
                    system("pause")    
                    self.menu_empleados_e()    
        except:
            print("ERROR AL INTENTAR LISTAR EMPLEADOS")
            system("pause")
            self.menu_empleados_e()

#------------------------------------------------------------------------------------- 

    def estadisticas_empleado_e(self):
            r = self.d.ListarEmpleados()
            if r is not None:
                system("cls")
                print("---------------------------------")
                print("-----Estadisticas Empleados------") 
                print("---------------------------------") 
                print(f"Cantidad Empleados                : { self.d.estadiscticasEmpleados(1) } ")
                print(f"Cantidad Empleados Habilitados    : { self.d.estadiscticasEmpleados(2) } ")
                print(f"Cantidad Empleados Suspendidos    : { self.d.estadiscticasEmpleados(3) } ")
                system("pause") 
                self.menu_empleados_e()
            else:
                print("No se Encuentran Registros de Empleados")

#-------------------------------------------------------------------------------------
#-------------------------------Menu para Empleados-----------------------------------
#------------------------------------proyectos---------------------------------------- 

    def menu_proyectos_e(self):
            try:
                system("cls")
                print("Gestion Proyectos")
                print("1- Listar Proyecto")
                print("2- Buscar Proyecto")
                print("3- Visualizar JSON")
                print("4- Salir")
                self.op_proyecto = int(input("Elija una Opcion: "))

                if self.op_proyecto == 1:
                    self.listar_proyecto_e()
                if self.op_proyecto == 2:
                    self.buscar_proyecto_e()
                if self.op_proyecto == 3:
                    self.VisualizarJson_e()             
                if self.op_proyecto == 4:
                    self.menu_e()
                else:
                    system("cls")
                    print("Error, Elija una Opcion")
                    system("pause")
                    self.menu_proyectos_e()
            except:
                print("Error al elegir opcion")
                system("pause")
                self.menu_proyectos_e()

#-------------------------------------------------------------------------------------

    def listar_proyecto_e(self):
        while True:
                try:
                    system("cls")
                    print("--------------------------------")
                    print("--------Listar Proyectos--------")
                    print("--------------------------------")
                    print("1- Listar Todos los Proyectos")
                    print("2- Listar Proyectos Habilitados")
                    print("3- Listar Proyectos Suspendidos")
                    print("4- Salir")
                    opl= int(input("Digite una de las Opciones: "))
                    if opl == 1:
                        system("cls")
                        print("--------------------------------")
                        print("---------Lista Proyectos--------")
                        print("--------------------------------")
                        r = self.d.listarProyecto()
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "TITULO", "DESCRIPCION", "FECHA", "ESTADO"]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4]] )
                
                            print(tabla)

                            system("pause")
                            self.menu_proyectos_e()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 2:
                        system("cls")
                        print("--------------------------------------------")
                        print("--------Lista Proyectos Hablilitados--------")
                        print("--------------------------------------------")
                        r = self.d.ListarProyectosHabilitados()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "TITULO", "DESCRIPCION", "FECHA", "ESTADO"]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4]] )
                
                            print(tabla)

                            system("pause")
                            self.menu_proyectos_e()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 3:
                        system("cls")
                        print("--------------------------------------------")
                        print("--------Lista Proyectos Suspendidos---------")
                        print("--------------------------------------------")
                        r = self.d.ListarProyectosSuspendidos()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "TITULO", "DESCRIPCION", "FECHA", "ESTADO"]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4]] )
                
                            print(tabla)

                            system("pause")
                            self.menu_proyectos_e()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 4:
                        self.menu_proyectos_e()
                    else:
                        print("ERROR, ELIJA UNA DE LAS OPCIONES")
                        system("pause")
                        self.listar_proyecto_e()
                except:
                    print("Error al Digitar Opcion")
                    system("pause")

#--------------------------------------------------------------------------

    def buscar_proyecto_e(self):
        system("cls")
        print("Buscar proyecto")
        tit = input("Ingrese titulo del proyecto: ")
        if len(tit.strip()) < 1 or len(tit.strip()) > 50:
                print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                system("pause")
                self.menu_proyectos_e()
        else:
            tit = tit.strip()
            r = self.d.buscarProyecto(tit)
            if r is not None:  
                print(f"Proyecto Encontrado!!!")
                print(f"ID PROYECTO: {r.getId_proyecto()}")
                print(f"TITULO: {r.getTitulo()}")
                print(f"DESCRIPCION: {r.getDescripcion()}")
                print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                system("pause")
                self.menu_proyectos_e()
            else:
                print("Este proyecto No Existe!!!")
                system("pause")    
                self.menu_proyectos_e()  

#-------------------------------------------------------------------------------------
    def VisualizarJson_e(self):
            system("cls")
            if not os.path.exists("pokedex.json"):
                print("Error, Json no Existe")
                system("pause")
                self.menu_proyectos_e()
            else:
                with open("pokedex.json", "r") as archivo:
                    dd = json.load(archivo)     
                    print(type(dd))
        
                tabla = BeautifulTable()
                tabla.columns.header = ["N° Pokedex","Nombre","Altura","Peso","Tipo 1","Tipo 2"]
                
                for x in dd:
                    tabla.rows.append( [x['id'],x['Nombre'],x['Altura'],x['Peso'], x['Tipo 1'], x['Tipo 2']] )  

                print(tabla)       
                system("pause")
                self.menu_proyectos_e()       

#-------------------------------------------------------------------------------------
#--------------------------------Menu para Gerentes-----------------------------------
#-------------------------------------------------------------------------------------
          
    def menu(self):
        try:
            system("cls")
            print("------------------------------")
            print("---------Menu Gerentes--------")
            print("------------------------------")
            print("1- Gestion Empleados")
            print("2- Gestion Proyectos")
            print("3- Cerra Cesion")
            self.op = int(input("Elija una Opcion: "))

            if self.op == 1:
                self.menu_empleados()
            if self.op == 2:
                self.menu_proyectos()
            if self.op == 3:
                self.menuMejorado()
            else:
                self.error_opcion()
        except:
            print("Error, Elija una Opcion Numerica")
            system("pause")
            self.menu()

#-------------------------------------------------------------------------------------
#--------------------------------Menu para Gerentes-----------------------------------
#-----------------------------------empleados-----------------------------------------

    def menu_empleados(self):
        try:
            system("cls")
            print("-------------------------------")
            print("-------Gestion Empleados-------")
            print("-------------------------------")
            print("1- Crear Empleado")
            print("2- Listar Empleado")
            print("3- Buscar Empleado")
            print("4- Modificar Empleado")
            print("5- Eliminar Empleado")
            print("6- Estadiscticas Empleado")
            print("7- Salir")
            self.op_empleados = int(input("Elija una Opcion: "))

            if self.op_empleados == 1:
                self.crear_empleado()
            if self.op_empleados == 2:
                self.listar_empleado()
            if self.op_empleados == 3:
                self.buscar_empleado()
            if self.op_empleados == 4:
                self.modificar_empleado()
            if self.op_empleados == 5:
                self.eliminar_empleado()
            if self.op_empleados == 6:
                self.estadisticas_empleado()             
            if self.op_empleados == 7:
                self.menu()
            else:
                system("cls")
                print("Error, Elija una Opcion")
                system("pause")
                self.menu_empleados()
        except:
            print("Error al elegir opcion")
            system("pause")
            self.menu()

#-------------------------------------------------------------------------------------

    def crear_empleado(self):
        try:
            system("cls")
            print("--------------------------------")
            print("-------Registro Empleados-------")
            print("--------------------------------")

            while True:
                try:
                    self.rut = input("Ingrese rut (Ej: 11.111.111-1): ")
                    if len(self.rut.strip()) < 1 or len(self.rut.strip()) > 50:
                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                        system("pause")
                        system("cls")
                    else:
                        self.rut = self.rut.strip()
                        r = self.d.comprobarEmpleado(self.rut)
                        if r is not None:
                            print(f"ERROR el Rut: {self.rut}, YA EXISTE!")
                            print("Intente con otra!")
                            system("pause")
                            system("cls")
                        else:
                            break
                except:
                    print("ERROR AL GUARDAR EL RUT")
                    system("pause")
                    system("cls")

            while True:
                try:
                    self.nom = input("Ingrese nombre: ")
                    if len(self.nom.strip()) < 1 or len(self.nom.strip()) > 50:
                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                        system("pause")
                        system("cls")
                    else:
                            break
                except:
                    print("ERROR AL GUARDAR EL NOMBRE")
                    system("pause")
                    system("cls")

            while True:
                try:
                    self.ape = input("Ingrese Apellido: ")
                    if len(self.ape.strip()) < 1 or len(self.ape.strip()) > 50:
                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                        system("pause")
                        system("cls")
                    else:
                            break
                except:
                    print("ERROR AL GUARDAR EL APELLIDO")
                    system("pause")
                    system("cls")

            while True:
                try:
                    self.eda = int(input("Ingrese Edad (Entre 18 y 65 Años): "))
                    if self.eda < 18 or self.eda > 65:
                        print("INGRESE EDAD DENTRO DEL RANGO")
                        system("pause")
                        system("cls")
                    else:
                            break
                except:
                    print("ERROR AL GUARDAR LA EDAD")
                    system("pause")
                    system("cls")

            while True:
                try:
                    self.fec = input("Ingrese fecha de inicio (Ej: 25/12/2022): ")
                    if len(self.fec.strip()) < 1 or len(self.fec.strip()) > 50:
                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                        system("pause")
                        system("cls")
                    else:
                        fecha_valida = datetime.strptime(self.fec, "%d/%m/%Y")
                        break
                except:
                    print("ERROR AL GUARDAR LA FECHA, DEBE TENER FORMATO DD/MM/AAAA.")
                    system("pause")
                    system("cls")

            while True:
                try:
                    self.sal = int(input("Ingrese salario: "))
                    if self.sal < 550000 or self.sal > 5000000:
                        print("Ingrese un Valor Entre 550.000 a 5.000.000")
                        system("pause")
                        system("cls")
                    else:
                            break
                except:
                    print("ERROR AL GUARDAR EL SALARIO")
                    system("pause")
                    system("cls")

            self.emp.setRut(self.rut)  
            self.emp.setNombre(self.nom.upper())
            self.emp.setApellido(self.ape.upper())
            self.emp.setEdad(self.eda)
            self.emp.setFecha_inicio(self.fec)
            self.emp.setSalario(self.sal)  
            self.emp.setId_Estado(1)
            self.d.agregarEmpleado(self.emp)
            system("cls")
            print("--------------------------------")
            print("----Se Agrego Nuevo Empleado----")
            print("--------------------------------")
            
            r = self.d.buscarEmpleado(self.rut)
            if r is not None:  
                system("cls")
                print(f"RUT: {r.getRut()}")
                print(f"NOMBRE: {r.getNombre()}")
                print(f"APELLIDO: {r.getApellido()}")
                print(f"EDAD: {r.getEdad()}")
                print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                print(f"SALARIO: {r.getSalario()}")
                print(f"Estado Empleado: {r.getNombre_Estado()}")
            system("pause")
            self.menu()
        except:
            print("ERROR AL INTENTAR CREAR EMPLEADOS")
            system("pause")
            system("cls")

#-------------------------------------------------------------------------------------

    def listar_empleado(self):
        while True:
            try:
                system("cls")
                print("--------------------------------")
                print("--------Listar Empleados--------")
                print("--------------------------------")
                print("1- Listar Todos los Empleado")
                print("2- Listar Empleados Habilitados")
                print("3- Listar Empleados Suspendidos")
                print("4- Salir")
                opl= int(input("Digite una de las Opciones: "))
                if opl == 1:
                    system("cls")
                    print("--------------------------------")
                    print("---------Lista Empleados--------")
                    print("--------------------------------")
                    r = self.d.ListarEmpleados()  
                    if r is not None: 
                        tabla = BeautifulTable()
                        tabla.columns.header = [ "ID", "RUT", "NOMBRE", "APELLIDO", "EDAD", "INICIO", "SALARIO", "ESTADO" ]
                        for x in r:
                            tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] ] )
            
                        print(tabla)

                        system("pause")
                        self.menu_empleados()
                    else:
                        print("ERROR, NO HAY EMPLEADOS")
                elif opl == 2:
                    system("cls")
                    print("--------------------------------------------")
                    print("--------Lista Empleados Hablilitados--------")
                    print("--------------------------------------------")
                    r = self.d.ListarEmpleadosHabilitados()  
                    if r is not None: 
                        tabla = BeautifulTable()
                        tabla.columns.header = [ "ID", "RUT", "NOMBRE", "APELLIDO", "EDAD", "INICIO", "SALARIO", "ESTADO" ]
                        for x in r:
                            tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] ] )
            
                        print(tabla)

                        system("pause")
                        self.menu_empleados()
                    else:
                        print("ERROR, NO HAY EMPLEADOS")
                elif opl == 3:
                    system("cls")
                    print("--------------------------------------------")
                    print("--------Lista Empleados Suspendidos---------")
                    print("--------------------------------------------")
                    r = self.d.ListarEmpleadosSuspendidos()  
                    if r is not None: 
                        tabla = BeautifulTable()
                        tabla.columns.header = [ "ID", "RUT", "NOMBRE", "APELLIDO", "EDAD", "INICIO", "SALARIO", "ESTADO" ]
                        for x in r:
                            tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] ] )
            
                        print(tabla)

                        system("pause")
                        self.menu_empleados()
                    else:
                        print("ERROR, NO HAY EMPLEADOS")
                elif opl == 4:
                    self.menu_empleados()
                else:
                    print("ERROR, ELIJA UNA DE LAS OPCIONES")
                    system("pause")
                    self.listar_empleado()
            except:
                print("Error al Digitar Opcion")
                system("pause")


#-------------------------------------------------------------------------------------

    def buscar_empleado(self):
        try:
            system("cls")
            print("--------------------------------")
            print("--------Buscar Empleados--------")
            print("--------------------------------")
            self.rut = input("Ingrese rut: ")
            if len(self.rut.strip()) < 1 or len(self.rut.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                    self.menu_empleados()
            else:
                self.rut = self.rut.strip()
                r = self.d.buscarEmpleado(self.rut)
                if r is not None:  
                    system("cls")
                    print(f"Empleado Encontrado!!!")
                    print(f"RUT: {r.getRut()}")
                    print(f"NOMBRE: {r.getNombre()}")
                    print(f"APELLIDO: {r.getApellido()}")
                    print(f"EDAD: {r.getEdad()}")
                    print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                    print(f"SALARIO: {r.getSalario()}")
                    print(f"Estado Empleado: {r.getNombre_Estado()}")
                    system("pause")
                    self.menu_empleados()
                else:
                    print("Este Rut No Existe!!!")
                    system("pause")    
                    self.menu_empleados()    
        except:
            print("ERROR AL INTENTAR LISTAR EMPLEADOS")
            system("pause")
            self.menu_empleados()

#-------------------------------------------------------------------------------------       

    def modificar_empleado(self):
        try:
            system("cls")
            print("-----------------------------------")
            print("--------Modificar Empleados--------")
            print("-----------------------------------")
            self.rut = input("Ingrese rut: ")
            if len(self.rut.strip()) < 1 or len(self.rut.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                    self.menu_empleados()
            else:
                self.rut = self.rut.strip()
                r = self.d.buscarEmpleado(self.rut)
                if r is not None:  
                    system("cls")
                    print(f"Empleado Encontrado!!!")
                    print(f"RUT: {r.getRut()}")
                    print(f"NOMBRE: {r.getNombre()}")
                    print(f"APELLIDO: {r.getApellido()}")
                    print(f"EDAD: {r.getEdad()}")
                    print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                    print(f"SALARIO: {r.getSalario()}")
                    print(f"Estado Empleado: {r.getNombre_Estado()}")
                    system("pause")
                    system("cls")
                    print("----------------------------------------")
                    print("--------Modificar Datos Empleado--------")
                    print("----------------------------------------")
                    print("1- Nombre 2- Apellido 3-Edad 4-Fecha de Inicio 5-Salario 6-Estado Trabajador 7-Cancelar" )
                    dato = int(input("Digite El Dato Que Desea Actualizar : "))
                    system("cls")
                    if dato<1 and dato>7:
                        print("Error De Opcion Al Intentar Actualizar Datos!!")
                        system("pause")
                        self.modificar_empleado()
                    else:
                        if dato == 1:
                            while True:
                                try:
                                    nuevo = input("Ingrese nombre: ")
                                    if len(nuevo.strip()) < 1 or len(nuevo.strip()) > 50:
                                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                                        system("pause")
                                        system("cls")
                                    else:
                                        self.d.modificarEmpleados(dato, nuevo.upper(), self.rut)
                                        print("Nombre Modificado")
                                        r = self.d.buscarEmpleado(self.rut)
                                        if r is not None:  
                                            system("pause")
                                            system("cls")
                                            print("Nuevos Datos Empleado")
                                            print(f"RUT: {r.getRut()}")
                                            print(f"NOMBRE: {r.getNombre()}")
                                            print(f"APELLIDO: {r.getApellido()}")
                                            print(f"EDAD: {r.getEdad()}")
                                            print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                                            print(f"SALARIO: {r.getSalario()}")
                                            print(f"Estado Empleado: {r.getNombre_Estado()}")
                                            system("pause")
                                        break
                                except:
                                    print("ERROR AL GUARDAR EL NOMBRE")
                                    system("pause")
                                    system("cls")

                        elif dato == 2:
                            while True:
                                try:
                                    nuevo= input("Ingrese Apellido: ")
                                    if len(nuevo.strip()) < 1 or len(nuevo.strip()) > 50:
                                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                                        system("pause")
                                        system("cls")
                                    else:
                                        self.d.modificarEmpleados(dato, nuevo.upper(), self.rut)
                                        print("Apellido Modificado")
                                        r = self.d.buscarEmpleado(self.rut)
                                        if r is not None:  
                                            system("pause")
                                            system("cls")
                                            print("Nuevos Datos Empleado")
                                            print(f"RUT: {r.getRut()}")
                                            print(f"NOMBRE: {r.getNombre()}")
                                            print(f"APELLIDO: {r.getApellido()}")
                                            print(f"EDAD: {r.getEdad()}")
                                            print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                                            print(f"SALARIO: {r.getSalario()}")
                                            print(f"Estado Empleado: {r.getNombre_Estado()}")
                                            system("pause")
                                        break
                                except:
                                    print("ERROR AL GUARDAR EL APELLIDO")
                                    system("pause")
                                    system("cls")
                

                        elif dato == 3:
                            while True:
                                try:
                                    nuevo = int(input("Ingrese Edad (Entre 18 y 65 Años): "))
                                    if nuevo < 18 or nuevo > 65:
                                        print("INGRESE EDAD DENTRO DEL RANGO")
                                        system("pause")
                                        system("cls")
                                    else:
                                        self.d.modificarEmpleados(dato, nuevo, self.rut)
                                        print("Edad Modificada")
                                        r = self.d.buscarEmpleado(self.rut)
                                        if r is not None:  
                                            system("pause")
                                            system("cls")
                                            print("Nuevos Datos Empleado")
                                            print(f"RUT: {r.getRut()}")
                                            print(f"NOMBRE: {r.getNombre()}")
                                            print(f"APELLIDO: {r.getApellido()}")
                                            print(f"EDAD: {r.getEdad()}")
                                            print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                                            print(f"SALARIO: {r.getSalario()}")
                                            print(f"Estado Empleado: {r.getNombre_Estado()}")
                                            system("pause")
                                        break
                                except:
                                    print("ERROR AL GUARDAR LA EDAD")
                                    system("pause")
                                    system("cls")

                        elif dato == 4:
                            while True:
                                try:
                                    nuevo = input("Ingrese fecha de inicio: ")
                                    if len(nuevo.strip()) < 1 or len(nuevo.strip()) > 50:
                                        print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                                        system("pause")
                                        system("cls")
                                    else:
                                        fecha_valida = datetime.strptime(nuevo, "%d/%m/%Y")
                                        self.d.modificarEmpleados(dato, nuevo, self.rut)
                                        print("Fecha de inicio Modificada")
                                        r = self.d.buscarEmpleado(self.rut)
                                        if r is not None:  
                                            system("pause")
                                            system("cls")
                                            print("Nuevos Datos Empleado")
                                            print(f"RUT: {r.getRut()}")
                                            print(f"NOMBRE: {r.getNombre()}")
                                            print(f"APELLIDO: {r.getApellido()}")
                                            print(f"EDAD: {r.getEdad()}")
                                            print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                                            print(f"SALARIO: {r.getSalario()}")
                                            print(f"Estado Empleado: {r.getNombre_Estado()}")
                                            system("pause")
                                        break
                                except:
                                    print("ERROR AL GUARDAR LA FECHA, DEBE TENER FORMATO DD/MM/AAAA.")
                                    system("pause")
                                    system("cls")

                        elif dato == 5:
                            while True:
                                try:
                                    nuevo = int(input("Ingrese salario: "))
                                    if nuevo < 1 or nuevo > 10000000:
                                        print("INGRESE UN VALOR VALIDO")
                                        system("pause")
                                        system("cls")
                                    else:
                                        self.d.modificarEmpleados(dato, nuevo, self.rut)
                                        print("Salario Modificado")
                                        r = self.d.buscarEmpleado(self.rut)
                                        if r is not None:  
                                            system("pause")
                                            system("cls")
                                            print("Nuevos Datos Empleado")
                                            print(f"RUT: {r.getRut()}")
                                            print(f"NOMBRE: {r.getNombre()}")
                                            print(f"APELLIDO: {r.getApellido()}")
                                            print(f"EDAD: {r.getEdad()}")
                                            print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                                            print(f"SALARIO: {r.getSalario()}")
                                            print(f"Estado Empleado: {r.getNombre_Estado()}")
                                            system("pause")
                                        break
                                except:
                                    print("ERROR AL GUARDAR EL SALARIO")
                                    system("pause")
                                    system("cls")
                    
                        elif dato == 6:
                            nuevo = 0
                            if r.getNombre_Estado() == "HABILITADO":
                                nuevo = 2
                            elif r.getNombre_Estado() == "SUSPENDIDO":
                                nuevo = 1
                            self.d.modificarEmpleados(dato, nuevo, self.rut)
                            print("Estado Modificado")
                            r = self.d.buscarEmpleado(self.rut)
                            if r is not None:  
                                system("pause")
                                system("cls")
                                print("Nuevos Datos Empleado")
                                print(f"RUT: {r.getRut()}")
                                print(f"NOMBRE: {r.getNombre()}")
                                print(f"APELLIDO: {r.getApellido()}")
                                print(f"EDAD: {r.getEdad()}")
                                print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                                print(f"SALARIO: {r.getSalario()}")
                                print(f"Estado Empleado: {r.getNombre_Estado()}")
                                system("pause")
                        elif dato == 7:
                            self.menu_empleados()
                        else:
                            print("ERROR, DIGITE UNA DE LAS OPCIONES")
                            system("pause")
                            self.modificar_empleado()
                    self.menu_empleados()
                else:
                    print("Este Rut No Existe!!!")
                    system("pause")    
                    self.menu_empleados()                     
        except:
            print("ERROR AL INTENTAR MODIFICAR EMPLEADO")
            system("pause")
            self.menu_empleados()
        
#-------------------------------------------------------------------------------------

    def eliminar_empleado(self):
        try:
            system("cls")
            print("----------------------------------")
            print("--------Eliminar Empleados--------")
            print("----------------------------------")
            self.rut = input("Ingrese rut: ")
            if len(self.rut.strip()) < 1 or len(self.rut.strip()) > 50:
                print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                system("pause")
                self.menu_empleados()
            else:
                self.rut = self.rut.strip()
                r = self.d.buscarEmpleado(self.rut)
                if r is not None:
                    system("cls")
                    print("Empleado Encontrado")
                    print(f"RUT: {r.getRut()}")
                    print(f"NOMBRE: {r.getNombre()}")
                    print(f"APELLIDO: {r.getApellido()}")
                    print(f"EDAD: {r.getEdad()}")
                    print(f"FECHA DE INICIO DE TRABAJO: {r.getFecha_inicio()}")
                    print(f"SALARIO: {r.getSalario()}")
                    print(f"Estado Empleado: {r.getNombre_Estado()}")
                    system("pause")

                    if r.getNombre_Estado() == "DESHABILITADO":
                        print(" El Empleado Ya Se Encuentra Eliminado!!")
                        system("pause")
                        self.menu_empleados()
                    else:
                        while True:
                            try:
                                op = int(input("¿Está Seguro(a) De Querer Eliminar al Empleado? (1.SI   2.NO) : "))
                                if op == 1:
                                    self.d.eliminarEmpleados(self.rut)
                                    print("Eliminando Empleado")
                                    system("pause")
                                    break
                                elif op == 2:
                                    break
                            except:
                                print("Error De Opcion De Eliminacion")
                                system("pause")
                    self.menu_empleados()
                else:
                    print("Este Rut No Existe!!!")
                    system("pause")    
                    self.menu_empleados()    
        except:
            print("ERROR AL INTENTAR ELIMINAR EMPLEADO")
            system("pause")
            self.menu_empleados()
#-------------------------------------------------------------------------------------

    def estadisticas_empleado(self):
        r = self.d.ListarEmpleados()
        if r is not None:
            system("cls")
            print("---------------------------------")
            print("-----Estadisticas Empleados------") 
            print("---------------------------------") 
            print(f"Cantidad Empleados                : { self.d.estadiscticasEmpleados(1) } ")
            print(f"Cantidad Empleados Habilitados    : { self.d.estadiscticasEmpleados(2) } ")
            print(f"Cantidad Empleados Suspendidos    : { self.d.estadiscticasEmpleados(3) } ")
            system("pause") 
            self.menu_empleados()
        else:
            print("No se Encuentran Registros de Empleados")

#-------------------------------------------------------------------------------------
#--------------------------------Menu para Gerentes-----------------------------------
#-----------------------------------proyectos-----------------------------------------

    def menu_proyectos(self):
        try:
            system("cls")
            print("Gestion Proyectos")
            print("1- Crear Proyecto")
            print("2- Listar Proyecto")
            print("3- Buscar Proyecto")
            print("4- Modificar Proyecto")
            print("5- Eliminar Proyecto")
            print("6- Consumir API")
            print("7- Visualizar JSON")
            print("8- Salir")
            self.op_proyecto = int(input("Elija una Opcion: "))

            if self.op_proyecto == 1:
                self.crear_proyecto()
            if self.op_proyecto == 2:
                self.listar_proyecto()
            if self.op_proyecto == 3:
                self.buscar_proyecto()
            if self.op_proyecto == 4:
                self.modificar_proyecto()
            if self.op_proyecto == 5:
                self.eliminar_proyecto()             
            if self.op_proyecto == 6:
                self.consumirAPI()
            if self.op_proyecto == 7:
                self.VisualizarJson()             
            if self.op_proyecto == 8:
                self.menu()
            else:
                system("cls")
                print("Error, Elija una Opcion")
                system("pause")
                self.menu_proyectos()
        except:
            print("Error al elegir opcion")
            system("pause")
            self.menu()

#-------------------------------------------------------------------------------------

    def crear_proyecto(self):

        system("cls")
        print("creacion de proyecto")

        while True:
            try:
                self.tit = input("Ingrese nombre del proyecto: ")
                if len(self.tit) < 1 or len(self.tit) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                else:
                    self.tit = self.tit
                    r = self.d.comprobarProyecto(self.tit)
                    if r is not None:
                        print(f"ERROR el TITULO: {self.tit}, YA EXISTE!")
                        print("Intente con otro nombre!")
                        system("pause")
                    else:
                        break
            except:
                print("ERROR AL GUARDAR EL NOMBRE Del PROYECTO")

        while True:
            try:
                self.desc = input("Ingrese la descripcion del proyecto: ")
                if len(self.desc) < 1 or len(self.desc) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                else:
                        break
            except:
                print("ERROR AL GUARDAR LA DESCRIPCION DEL PROYECTO")
    
        while True:
            try:
                self.ini = input("Ingrese inicio del proyecto (EJ: 21/11/2025): ")
                if len(self.ini.strip()) < 1 or len(self.ini.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                else:
                    fecha_valida = datetime.strptime(self.ini, "%d/%m/%Y")
                    break
            except:
                print("ERROR AL GUARDAR EL INICIO DEL PROYECTO DEBE TENER FORMATO DD/MM/AA")

        self.pro.setTitulo(self.tit)
        self.pro.setDescripcion(self.desc)
        self.pro.setInicio_proyecto(self.ini)
        self.pro.setId_Estado(1)
        self.d.agregarProyecto(self.pro)
        system("cls")
        print("Se agrego nuevo proyecto...  ")
        system("pause")
        self.menu_proyectos()

#-------------------------------------------------------------------------------------

    def listar_proyecto(self):
        while True:
                try:
                    system("cls")
                    print("--------------------------------")
                    print("--------Listar Proyectos--------")
                    print("--------------------------------")
                    print("1- Listar Todos los Proyectos")
                    print("2- Listar Proyectos Habilitados")
                    print("3- Listar Proyectos Suspendidos")
                    print("4- Salir")
                    opl= int(input("Digite una de las Opciones: "))
                    if opl == 1:
                        system("cls")
                        print("--------------------------------")
                        print("---------Lista Proyectos--------")
                        print("--------------------------------")
                        r = self.d.listarProyecto()
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "TITULO", "DESCRIPCION", "FECHA", "ESTADO"]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4]] )
                
                            print(tabla)

                            system("pause")
                            self.menu_proyectos()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 2:
                        system("cls")
                        print("--------------------------------------------")
                        print("--------Lista Proyectos Hablilitados--------")
                        print("--------------------------------------------")
                        r = self.d.ListarProyectosHabilitados()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "TITULO", "DESCRIPCION", "FECHA", "ESTADO"]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4]] )
                
                            print(tabla)

                            system("pause")
                            self.menu_proyectos()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 3:
                        system("cls")
                        print("--------------------------------------------")
                        print("--------Lista Proyectos Suspendidos---------")
                        print("--------------------------------------------")
                        r = self.d.ListarProyectosSuspendidos()  
                        if r is not None: 
                            tabla = BeautifulTable()
                            tabla.columns.header = [ "ID", "TITULO", "DESCRIPCION", "FECHA", "ESTADO"]
                            for x in r:
                                tabla.rows.append( [ x[0], x[1], x[2], x[3], x[4]] )
                
                            print(tabla)

                            system("pause")
                            self.menu_proyectos()
                        else:
                            print("ERROR, NO HAY EMPLEADOS")
                    elif opl == 4:
                        self.menu_proyectos()
                    else:
                        print("ERROR, ELIJA UNA DE LAS OPCIONES")
                        system("pause")
                        self.listar_proyecto()
                except:
                    print("Error al Digitar Opcion")
                    system("pause")

#--------------------------------------------------------------------------

    def buscar_proyecto(self):
        system("cls")
        print("Buscar proyecto")
        tit = input("Ingrese titulo del proyecto: ")
        if len(tit.strip()) < 1 or len(tit.strip()) > 50:
                print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                system("pause")
                self.menu_proyectos()
        else:
            tit = tit.strip()
            r = self.d.buscarProyecto(tit)
            if r is not None:  
                print(f"Proyecto Encontrado!!!")
                print(f"ID PROYECTO: {r.getId_proyecto()}")
                print(f"TITULO: {r.getTitulo()}")
                print(f"DESCRIPCION: {r.getDescripcion()}")
                print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                system("pause")
                self.menu_proyectos()
            else:
                print("Este proyecto No Existe!!!")
                system("pause")    
                self.menu_proyectos()  

#-------------------------------------------------------------------------------------
    def modificar_proyecto(self):
        try:

            system("cls")
            print("Modificacion de Proyecto")
            tit = input("Ingrese Titulo del proyecto: ")
            if len(tit.strip()) < 1 or len(tit.strip()) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                    self.menu_proyectos()
            else:
                tit = tit.strip()
                r = self.d.buscarProyecto(tit)
                if r is not None:  
                    system("cls")
                    print(f"Proyecto Encontrado!!!")
                    print(f"TITULO: {r.getTitulo()}")
                    print(f"DESCRIPCION: {r.getDescripcion()}")
                    print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                    print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                    system("pause")
                    print("cls")
                    print("---------------------------------")
                    print("---Modificar Datos de proyecto---")
                    print("---------------------------------")
                    print("elija que apartado modificar")
                    print("1.- Descripcion")
                    print("2.- Fecha de inicio")
                    print("3.- Estado")
                    print("4.- Salir")
                    dato = int(input("digite la opcion a elegir: "))                  
                    if dato == 1:
                        while True:
                            system("cls")
                            try: 
                                nuevo = input("Ingrese descripcion: ")
                                if len(nuevo) < 1 or len(nuevo) > 50:
                                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                                    system("pause")
                                else:
                                    self.d.modificarProyecto(dato, nuevo, tit)
                                    system("cls")
                                    print("Se Modifico la Descripcion")
                                    r = self.d.buscarProyecto(tit)
                                    if r is not None:  
                                        system("pause")
                                        system("cls")
                                        print(f"ID PROYECTO: {r.getId_proyecto()}")
                                        print(f"TITULO: {r.getTitulo()}")
                                        print(f"DESCRIPCION: {r.getDescripcion()}")
                                        print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                                        print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                                        system("pause")
                                        break
                                    else:
                                        print("Este proyecto No Existe!!!")
                                        system("pause")    
                                        self.menu_proyectos()
                            except:
                                print("ERROR AL GUARDAR LA DESCRIPCION")
                        self.menu_proyectos()

                    elif dato == 2:
                        while True:
                            system("cls")
                            try:
                                nuevo = input("Ingrese fecha de inicio: ")
                                if len(nuevo.strip()) < 1 or len(nuevo.strip()) > 50:
                                    print("INGRESE UNA FECHA VALIDA")
                                    system("pause")
                                else:
                                    fecha_valida = datetime.strptime(nuevo, "%d/%m/%Y")
                                    r.setInicio_proyecto(nuevo)
                                    self.d.modificarProyecto(dato, nuevo, tit)
                                    system("cls")
                                    print("Se Modifico Fecha de Inicio ")
                                    r = self.d.buscarProyecto(tit)
                                    if r is not None:  
                                        system("pause")
                                        system("cls")
                                        print(f"ID PROYECTO: {r.getId_proyecto()}")
                                        print(f"TITULO: {r.getTitulo()}")
                                        print(f"DESCRIPCION: {r.getDescripcion()}")
                                        print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                                        print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                                        system("pause")
                                        break
                                    
                                self.menu_proyectos()
                            except:
                                print("ERROR AL GUARDAR LA FECHA, DEBE TENER FORMATO DD/MM/AAAA.")
                                system("pause")
                        self.menu_proyectos()
                    
                    elif dato == 3:
                                system("cls")
                                nuevo = 0
                                if r.getNombre_Estado() == "HABILITADO":
                                    nuevo = 2
                                elif r.getNombre_Estado() == "DESHABILITADO":
                                    nuevo = 1
                                self.d.modificarProyecto(dato, nuevo, tit)
                                print("Estado Modificado")
                                r = self.d.buscarProyecto(tit)
                                if r is not None:  
                                    system("pause")
                                    system("cls")
                                    print(f"ID PROYECTO: {r.getId_proyecto()}")
                                    print(f"TITULO: {r.getTitulo()}")
                                    print(f"DESCRIPCION: {r.getDescripcion()}")
                                    print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                                    print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                                    system("pause")
                                    self.menu_proyectos()
                                else:
                                    print("Este proyecto No Existe!!!")
                                    system("pause")   
                                    system("cls") 
                                    self.menu_proyectos()
                           
                    elif dato == 4:
                        self.menu_proyectos()
                    else:
                        print("Digite una de las Opciones")
                        system("pause")
                        system("cls")
                        self.menu_proyectos()

                else:
                    print("Este Proyecto No Existe!!!")
                    system("pause")    
                    self.menu_proyectos()  
        except:
            print("ERROR AL INTENTAR MODIFICAR PROYECTO")
            system("pause")
            self.menu_proyectos()
#----------------------------------------  

#-------------------------------------------------------------------------------------

    def eliminar_proyecto(self):
        try:
            system("cls")
            print("----------------------------------")
            print("--------Eliminar Proyecto--------")
            print("----------------------------------")
            tit = input("Ingrese titulo del proyecto: ")
            if len(tit) < 1 or len(tit) > 50:
                    print("ERROR DEBE TENER ENTRE 1 Y 50 CARACTERES")
                    system("pause")
                    self.menu_proyectos()
            else:
                tit = tit
                r = self.d.buscarProyecto(tit)
                if r is not None:
                    print(f"Proyecto Encontrado!!!")
                    print(f"ID PROYECTO: {r.getId_proyecto()}")
                    print(f"TITULO: {r.getTitulo()}")
                    print(f"DESCRIPCION: {r.getDescripcion()}")
                    print(f"FECHA DE INICIO: {r.getInicio_proyecto()}")
                    print(f"ESTADO PROYECTO: {r.getNombre_Estado()}")
                    system("pause")

                    if r.getNombre_Estado() == "DESHABILITADO":
                        print(" El Proyecto Ya Se Encuentra Eliminado!!")
                        system("pause")
                        self.menu_proyectos()
                    else:
                        while True:
                            try:
                                op = int(input("¿Está Seguro(a) De Querer Eliminar el Proyecto? (1.SI   2.NO) : "))
                                if op == 1:
                                    self.d.eliminarProyectos(tit)
                                    print("Eliminando Proyecto")
                                    system("pause")
                                    break
                                elif op == 2:
                                    break
                            except:
                                print("Error De Opcion De Eliminacion")
                                system("pause")
                    self.menu_proyectos()
                else:
                    print("Este Rut No Existe!!!")
                    system("pause")    
                    self.menu_proyectos()    
        except:
            print("ERROR AL INTENTAR ELIMINAR PROYECTO")
            system("pause")
            self.menu_proyectos()
#-------------------------------------------------------------------------------------
    def consumirAPI(self):
        system("cls")
        Requests.requestPokemon()    
        system("pause")
        self.menu_proyectos()

    def VisualizarJson(self):
        system("cls")
        if not os.path.exists("pokedex.json"):
            print("Error, Json no Existe")
            system("pause")
            self.menu_proyectos()
        else:
            with open("pokedex.json", "r") as archivo:
                dd = json.load(archivo)     
                print(type(dd))
     
            tabla = BeautifulTable()
            tabla.columns.header = ["N° Pokedex","Nombre","Altura","Peso","Tipo 1","Tipo 2"]
            
            for x in dd:
                tabla.rows.append( [x['id'],x['Nombre'],x['Altura'],x['Peso'], x['Tipo 1'], x['Tipo 2']] )  

            print(tabla)       
            system("pause")
            self.menu_proyectos()
        
         
#-------------------------------------------------------------------------------------

    """ def estadisticas_proyecto(self):
        system("cls")
        print("Estadisticas Proyectos")
        r = self.d.estadisticasProyectos()
        if r is None:
            print("NO HAY PROYECTOS")     
            system("pause") 
            self.menu_proyectos()  
        else:
            print(f"Numero de Proyectos: {r}")
            system("pause")
            self.menu_proyectos()  """

    """ def visualizar_empleado(self):
        print("Visualizacion Empleados por Proyectos")
        if len(lista2) == 0:
            print("NO EXISTEN PROYECTOS REGISTRADOS")
            system("pause")
            self.menu_proyectos
        else:
            buscar_proyecto = input("Ingrese el Titulo del Proyecto: ")
            for x in lista2:
                if buscar_proyecto == x.getTitulo():
                    system("cls")
                    print(f"Titulo   :  {x.getTitulo()}")
                    print(f"Descripcion   :  {x.getDescripcion()}")
                    print(f"Inicio de Proyecto: {x.getInicio_proyecto()}")
                    print(f"Rut Empleado    {x.getRut()}")
                    print(f"Nombre Empleado:  ")
                    print("============================================")
                    system("pause")
                    self.menu_proyectos()
            print("NO EXISTEN PROYECTO REGISTRADOS")
        system("pause")
        self.menu_proyectos() """

    def salir(self):   
        print("Saliendo del Programa...")
        system("cls")
        os._exit(1)
        

    def error_opcion(self):
        print("ERROR DE OPCION EN EL MENU")
        system("pause")
        self.menu()  