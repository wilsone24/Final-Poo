from Entidades.Empresa import Empresa
from Entidades.Empleados import Conductor
from Entidades.Empleados import Asistente
from Funcionalidades.Recoleccion import recoleccion_Diaria
from Funcionalidades.PuntoGeografico import puntos_geograficos
from Funcionalidades.Turnos import Turno

def main():
    Productos = ["vidrio","papel","plastico","metal","residuos organicos"]
    empresa1 = Empresa("Uninorte",111111)
    conductor = Conductor("Juan",123456)
    asistente1 = Asistente("Pedro",654321)
    asistente2 = Asistente("Maria",987654)
    empresa1.GenerarCamion("ABC123","Volvo")
    empresa1.GenerarCamion("DEF456","Mercedes")
    recoleccion1 = recoleccion_Diaria(empresa1)
    turno1 = Turno(conductor, asistente1, asistente2, empresa1.camiones["ABC123"],"8:00","12:00", None, recoleccion1)
    print(turno1)
    print()
    puntos_geograficos1 = puntos_geograficos(1,2,Productos[0],100)
    puntos_geograficos2 = puntos_geograficos(3,4,Productos[3],3400)
    puntos_geograficos3 = puntos_geograficos(5,6,Productos[0],300)
    puntos_geograficos4 = puntos_geograficos(7,8,Productos[0],400)
    turno1.ruta=[puntos_geograficos1,puntos_geograficos2,puntos_geograficos3,puntos_geograficos4]
    turno1.recolectar()
    turno1.recoleccion_Diaria.get_Residuos_Obtenidos()