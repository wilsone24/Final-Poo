from Entidades.Camiones import Camion

class Empresa: 
    
    def __init__(self, nombre:str, id:int) -> None:
        """Constructor de la clase Empresa

        Args:
            nombre (str): Nombre de la empresa
            id (int): identificador unico
        """
        Empresa.__instance = self
        self.__nombre = nombre
        self.id = id
        self.camiones = dict({}) 
        self.empleados = dict({})        

    @staticmethod
    def get_instance()->None:
        """Metodo para obtener la unica instancia de la clase empresa
        """
        if Empresa.__instance is None:
            Empresa()
        return Empresa.__instance
    
    def Contratar_empleado(self,empleado:object)-> None:
        """Metodo para asignar empleados a la empresa

        Args:
            empleado (object): empleado que será asignado a la empresa
        """
        self.empleados.update({empleado.nombre:empleado})

    def GenerarCamion(self, placa:str, modelo:str)-> None:
        """Funcion Para generar camiones que se almacenaran en la empresa

        Args:
            placa (str): Nombre de la empresa
            modelo (str): El modelo del camion
        """
        camion = Camion(placa,modelo)
        self.camiones.update({placa:camion})
        
    @property 
    def nombre(self)->str:
        """Funcion Para acceder al nombre de la empresa

        Returns:
            str: Nombre de la empresa
        """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo:str)->None:
        """Funcion para definir un nuevo nombre para la empresa

        Args:
            nuevo (str): Nuevo nombre de la empresa

        """
        self.__nombre = nuevo