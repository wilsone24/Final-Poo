import unittest
from RecursoTest.Emp_test import Empresa
from Entidades.Empleados import Conductor
from Entidades.Empleados import Asistente
from Funcionalidades.Recoleccion import recoleccion_Diaria
from Funcionalidades.PuntoGeografico import puntos_geograficos
from Funcionalidades.Turnos import Turno


class TestEmpresa(unittest.TestCase):

    def setUp(self):
        """Funcion para inicializar lo necesario en las pruebas unitarias
        """
        self.Productos = ["vidrio","papel","plastico","metal","residuos organicos"]
        self.empresa = Empresa("Uninorte", 1234561)
        self.conductor = Conductor("Juan", 123456)
        self.asistente1 = Asistente("Pedro", 654321)
        self.asistente2 = Asistente("Maria", 987654)
        self.empresa.Contratar_empleado(self.conductor)
        self.empresa.Contratar_empleado(self.asistente1)
        self.empresa.Contratar_empleado(self.asistente2)
        self.empresa.GenerarCamion("IRV993", "FORD")
        self.empresa.GenerarCamion("CWL088", "CHEVROLET")
        self.empresa.GenerarCamion("HYU345", "HYUNDAI")
        
        self.recoleccion1 = recoleccion_Diaria(self.empresa)
        self.recoleccion3 = recoleccion_Diaria(self.empresa)
    
        self.turno1 = Turno(self.empresa.empleados["Juan"], self.empresa.empleados["Pedro"], self.empresa.empleados["Maria"], self.empresa.camiones["IRV993"], "8:00", "12:00", None, self.recoleccion1)
        self.turno3 = Turno(self.empresa.empleados["Juan"], self.empresa.empleados["Pedro"], self.empresa.empleados["Maria"], self.empresa.camiones["IRV993"], "14:00", "18:00", None, self.recoleccion3)
        
        self.punto1 = puntos_geograficos("Barranquilla", 1, 2, self.Productos[0], 100)
        self.punto2 = puntos_geograficos("Medellin", 3, 4, self.Productos[3], 200)
        self.punto3 = puntos_geograficos("Ocaña", 5, 6, self.Productos[2], 300)
        self.punto4 = puntos_geograficos("Cartagena", 7, 8, self.Productos[1], 300)

        self.punto9 = puntos_geograficos("Barranquilla", 1, 2, self.Productos[0], 159)
        self.punto10 = puntos_geograficos("Santa Marta", 3, 4, self.Productos[3], 650)
        self.punto11 = puntos_geograficos("Bogota", 5, 6, self.Productos[2], 50)
        self.punto12 = puntos_geograficos("Valledupar", 7, 8, self.Productos[1], 350)

        self.turno1.ruta = [self.punto1, self.punto2, self.punto3, self.punto4]
        self.turno3.ruta = [self.punto9, self.punto10, self.punto11, self.punto12]

    def test_recolectar(self):
        """Funcion que permite hacer teste de la funcion recolectar
        """
        self.turno1.recolectar()
        self.assertEqual(self.recoleccion1.cantidad_vidrio, 100)
        self.assertEqual(self.recoleccion1.cantidad_papel, 300)
        self.assertEqual(self.recoleccion1.cantidad_plastico, 300)
        self.assertEqual(self.recoleccion1.cantidad_metal, 200)
        self.assertEqual(self.recoleccion1.cantidad_residuos_organicos, 0)
        self.assertEqual(self.turno1.carga_recogida, 900)


    def test_recolectar3(self):
        """Funcion que permite hacer teste de la funcion recolectar
        """
        self.turno3.recolectar()
        self.assertEqual(self.recoleccion3.cantidad_vidrio, 159)
        self.assertEqual(self.recoleccion3.cantidad_papel, 350)
        self.assertEqual(self.recoleccion3.cantidad_plastico, 50)
        self.assertEqual(self.recoleccion3.cantidad_metal, 650)
        self.assertEqual(self.recoleccion3.cantidad_residuos_organicos, 0)
        self.assertEqual(self.turno3.carga_recogida, 1209)

    def test_Contratar_empleado(self):
        """Funcion que permite hacer teste de la funcion Contratar Empleado
        """
        self.assertEqual(len(self.empresa.empleados), 3)
        self.assertEqual(self.empresa.empleados["Juan"].nombre, "Juan")
        self.assertEqual(self.empresa.empleados["Pedro"].nombre, "Pedro")
        self.assertEqual(self.empresa.empleados["Maria"].nombre, "Maria")

    def test_GenerarCamion(self):
        """Funcion que permite hacer teste de la funcion Generar Camion
        """
        self.assertEqual(len(self.empresa.camiones), 3)
        self.assertEqual(self.empresa.camiones["IRV993"].modelo, "FORD")

    def test_GenerarCamion(self):
        """Funcion que permite hacer teste de la funcion Generar Camion
        """
        self.assertEqual(len(self.empresa.camiones), 3)
        self.assertEqual(self.empresa.camiones["CWL088"].modelo, "CHEVROLET")

    def test_GenerarCamion(self):
        """Funcion que permite hacer teste de la funcion Generar Camion
        """
        self.assertEqual(len(self.empresa.camiones), 3)
        self.assertEqual(self.empresa.camiones["HYU345"].modelo, "HYUNDAI")

    
if __name__ == '__main__':
    unittest.main()