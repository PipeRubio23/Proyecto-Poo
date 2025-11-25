from Personas import Personas
from Usuario import Usuario
from Empleados import Empleados
from Proyectos import Proyectos
from os import system;
import pymysql

class DAO:

    def __init__(self):
        pass

#-----------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "bd_gerentes"
        )
        self.cursor = self.con.cursor()

#-----------------------------------------------------

    def desconectar(self):
        self.con.close()

#-----------------------------------------------------

    def iniciosecion(self, nom):
        try:
            sql = "select nom_usu, con_usu from usuario where nom_usu = %s"
            self.conectar()
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()

            if rs is None:
                return None
            else:
                usu = Usuario()
                usu.setNombre_perfil(rs[0])
                usu.setContraseña(rs[1])
                return usu
        except Exception as e:
            print(f"Error al comprobar Rut (DAO) {e}")
            system("pause")
#-----------------------------------------------------

    def comprobarEmpleado(self, rut):
        try:
            sql = "select rut_emp from empleados where rut_emp=%s"
            self.conectar()
            self.cursor.execute(sql, rut)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except Exception as e:
            print(f"Error al comprobar Rut (DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------    

    def agregarEmpleado(self, emp):
        try:
            sql = "insert into empleados (rut_emp, nom_emp, ape_emp, eda_emp, fec_emp, sal_emp, id_est) values (%s, %s, %s, %s, %s, %s,%s)"
            val = (emp.getRut(), emp.getNombre(), emp.getApellido(), emp.getEdad(), emp.getFecha_inicio(), emp.getSalario(), emp.getId_Estado())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            print(f"ERROR AL AGREGAR UNA EMPLEADO (DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------

    def ListarEmpleados(self):
        try:
            sql = "select id_emp, rut_emp, nom_emp, ape_emp, eda_emp, fec_emp, sal_emp, nom_est from empleados e inner join estados est on e.id_est=est.id_est"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs        
        except Exception as e:
            print(f"ERROR EN OBTENER EMPLEADO (DAO) {e}")
            system("pause")

    def ListarEmpleadosHabilitados(self):
        try:
            sql = "select id_emp, rut_emp, nom_emp, ape_emp, eda_emp, fec_emp, sal_emp, nom_est from empleados e inner join estados est on e.id_est=est.id_est where e.id_est=1"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs        
        except Exception as e:
            print(f"ERROR EN OBTENER EMPLEADO (DAO) {e}")
            system("pause")

    def ListarEmpleadosSuspendidos(self):
        try:
            sql = "select id_emp, rut_emp, nom_emp, ape_emp, eda_emp, fec_emp, sal_emp, nom_est from empleados e inner join estados est on e.id_est=est.id_est where e.id_est=2"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs        
        except Exception as e:
            print(f"ERROR EN OBTENER EMPLEADO (DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------

    def buscarEmpleado(self, rut):
        try:
            sql = "select rut_emp, nom_emp, ape_emp, eda_emp, fec_emp, sal_emp, nom_est from empleados e inner join estados est on e.id_est=est.id_est where rut_emp=%s"
            self.conectar()
            self.cursor.execute(sql, rut)
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return None
            else:
                emp = Empleados()
                emp.setRut(rs[0])
                emp.setNombre(rs[1])
                emp.setApellido(rs[2])
                emp.setEdad(rs[3])
                emp.setFecha_inicio(rs[4])
                emp.setSalario(rs[5])
                emp.setNombre_Estado(rs[6])
                return emp
            
        except Exception as e:
            print(f"ERROR AL BUSCAR LA EMPLEADO (DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------

    def modificarEmpleados(self, dato, nuevo, rut):
        try:
            sql = ""
            if dato == 1:
                sql = "update empleados set nom_emp=%s where rut_emp=%s"
            elif dato == 2:
                sql = "update empleados set ape_emp=%s where rut_emp=%s"
            elif dato == 3:
                sql = "update empleados set eda_emp=%s where rut_emp=%s"
            elif dato == 4:
                sql = "update empleados set fec_emp=%s where rut_emp=%s"
            elif dato == 5:
                sql = "update empleados set sal_emp=%s where rut_emp=%s"
            elif dato == 6:
                sql = "update empleados set id_est=%s where rut_emp=%s"

            self.conectar()
            val = (nuevo, rut)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            print(f"ERROR AL ACTUALIZAR DATOS DE EMPLEADO(DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------

    def eliminarEmpleados(self, rut):
        try:
            sql = "update empleados set id_est=%s where rut_emp = %s"
            self.conectar()
            val = (2, rut)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            print(f"ERROR EN ELIMINAR EMPLEADO (DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------

    def estadiscticasEmpleados(self, opcion):
        try:
            sql = ""
            if opcion == 1:
                sql = "select count(*) from empleados"
            elif opcion == 2:
                sql = "select count(*) from empleados where id_est=1"
            elif opcion == 3:
                sql = "select count(*) from empleados where id_est=2"
            
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs[0]
        except Exception as e:
            print(f"ERROR AL OBTENER ESTADISTICAS!! (DAO) {e}")
            system("pause")

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------proyectos----------------------------------------

    def agregarProyecto(self, pro):
            try:
                sql = "insert into proyectos (tit_pro, des_pro, fec_pro, id_est) values (%s, %s, %s, %s)"
                val = (pro.getTitulo(), pro.getDescripcion(), pro.getInicio_proyecto(), pro.getId_Estado())
                self.conectar()
                self.cursor.execute(sql, val)
                self.con.commit()
                self.desconectar()
            except Exception as e:
                print(f"ERROR AL AGREGAR UN PROYECTO (DAO) {e}")
                system("pause")

    #----------------------------------------------------------------------------------

    def comprobarProyecto(self, tit):
        try:
            sql = "select tit_pro from proyectos where tit_pro=%s"
            self.conectar()
            self.cursor.execute(sql, tit)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except Exception as e:
            print(f"Error al comprobar nombre de titulo (DAO) {e}")
            system("pause")

    #----------------------------------------------------------------------------------
    def listarProyecto(self):
        try:
            sql= "select id_pro, tit_pro, des_pro, fec_pro, nom_est from proyectos p inner join estados est on p.id_est=est.id_est"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs        
        except Exception as e:
            print(f"ERROR EN OBTENER EMPLEADO (DAO) {e}")
            system("pause")

    def ListarProyectosHabilitados(self):
        try:
            sql= "select id_pro, tit_pro, des_pro, fec_pro, nom_est from proyectos p inner join estados est on p.id_est=est.id_est where p.id_est=1"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs        
        except Exception as e:
            print(f"ERROR EN OBTENER PROYECTO (DAO) {e}")
            system("pause")

    def ListarProyectosSuspendidos(self):
        try:
            sql= "select id_pro, tit_pro, des_pro, fec_pro, nom_est from proyectos p inner join estados est on p.id_est=est.id_est where p.id_est=2"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs        
        except Exception as e:
            print(f"ERROR EN OBTENER PROYECTO (DAO) {e}")
            system("pause")

    #----------------------------------------------------------------------------------

    def buscarProyecto(self, tit):
        
        try:
            sql = "select id_pro, tit_pro, des_pro, fec_pro, nom_est from proyectos p inner join estados est on p.id_est=est.id_est where tit_pro=%s"
            self.conectar()
            self.cursor.execute(sql, tit)
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return None
            else:
                pro = Proyectos()
                pro.setId_proyecto(rs[0])
                pro.setTitulo(rs[1])
                pro.setDescripcion(rs[2])
                pro.setInicio_proyecto(rs[3])
                pro.setNombre_Estado(rs[4])
                return pro
        except Exception as e:
            print(f"ERRROR AL BUSCAR PROYECTOS (DAO) {e}")
            system("pause")

    #----------------------------------------------------------------------------------

    def modificarProyecto(self, dato, nuevo, tit):
        try:
            sql = ""
            if dato == 1:
                sql = "update proyectos set des_pro=%s where tit_pro=%s"
            elif dato == 2:
                sql = "update proyectos set fec_pro=%s where tit_pro=%s"
            elif dato == 3:
                sql = "update proyectos set id_est=%s where tit_pro=%s"

            self.conectar()
            val = (nuevo, tit)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            print(f"ERROR AL ACTUALIZAR DATOS DE PROYECTO (DAO) {e}")
            system("pause")

    #----------------------------------------------------------------------------------

    def eliminarProyectos(self, tit):
        try:
            sql = "update proyectos set id_est=%s where tit_pro = %s"
            self.conectar()
            val = (2, tit)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            print("ERROR EN ELIMINAR PROYECTO (DAO) {e}")
            system("pause")

    #----------------------------------------------------------------------------------

    def estadisticasProyectos(self):
        try:
            sql = "select count(*) from proyectos"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
        except:
            print("ERROR CONTAR PROYECTOS (DAO)")
            system("pause")