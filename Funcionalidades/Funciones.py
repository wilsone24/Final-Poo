from Entidades.Empresa import Empresa
from Entidades.Empleados import Conductor
from Entidades.Empleados import Asistente
from Funcionalidades.Recoleccion import recoleccion_Diaria
from Funcionalidades.PuntoGeografico import puntos_geograficos
from Funcionalidades.Turnos import Turno

def main():
    """Funcion que ejecuta el programa principal
    """
    Productos = ["vidrio","papel","plastico","metal","residuos organicos"]
    empresa1 = Empresa("Uninorte",111111)
    conductor = Conductor("Juan",123456)
    asistente1 = Asistente("Pedro",654321)
    asistente2 = Asistente("Maria",987654)
    empresa1.Contratar_empleado(conductor)
    empresa1.Contratar_empleado(asistente1)
    empresa1.Contratar_empleado(asistente2)
    empresa1.GenerarCamion("IRV993","FORD")
    empresa1.GenerarCamion("FSK129","CHEVROLET")
    recoleccion1 = recoleccion_Diaria(empresa1)
    recoleccion2 = recoleccion_Diaria(empresa1)
    turno1 = Turno(empresa1.empleados["Juan"], empresa1.empleados["Pedro"], empresa1.empleados["Maria"], empresa1.camiones["IRV993"],"8:00","12:00", None, recoleccion1)
    turno2 = Turno(empresa1.empleados["Juan"], empresa1.empleados["Pedro"], empresa1.empleados["Maria"], empresa1.camiones["FSK129"],"13:00","17:00", None, recoleccion2)
    punto1 = puntos_geograficos("Barranquilla",1,2,Productos[0],1900)
    punto2 = puntos_geograficos("Medellin",3,4,Productos[3],1400)
    punto3 = puntos_geograficos("Ocaña",5,6,Productos[2],300)
    punto4 = puntos_geograficos("Cartagena",7,8,Productos[1],400)
    punto5 = puntos_geograficos("Barranquilla",1,2,Productos[0],100)
    punto6 = puntos_geograficos("Santa Marta",3,4,Productos[3],1400)
    punto7 = puntos_geograficos("Bogota",5,6,Productos[2],1300)
    punto8 = puntos_geograficos("Valledupar",7,8,Productos[1],500)
    turno1.ruta=[punto1,punto2,punto3,punto4]
    turno2.ruta=[punto5,punto6,punto7,punto8]
    print()
    recoleccion1.suscribirse(turno1)
    recoleccion2.suscribirse(turno2)
    print(f'------ TURNO 1 ------')
    print()
    print(turno1)
    turno1.recolectar()
    print()
    print(f'------ TURNO 2 ------')
    print()
    print(turno2)
    turno2.recolectar()
    print()
    print()
    print("La empresa recolecto en total en los dos turnos de recolección:")
    print(f"Vidrio: {recoleccion1.cantidad_vidrio + recoleccion2.cantidad_vidrio}")
    print(f"Papel: {recoleccion1.cantidad_papel + recoleccion2.cantidad_papel}")
    print(f"Plastico: {recoleccion1.cantidad_plastico + recoleccion2.cantidad_plastico}")
    print(f"Metal: {recoleccion1.cantidad_metal + recoleccion2.cantidad_metal}")
    print(f"Residuos Organicos: {recoleccion1.cantidad_residuos_organicos + recoleccion2.cantidad_residuos_organicos}")
    print()


