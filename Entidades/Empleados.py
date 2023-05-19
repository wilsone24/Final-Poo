class Empleado:
    def __init__(self, nombre:str, id:int) -> None:
        """Constructor de la clase Empleado

        Args:
            tipo (str): Tipo de empleado
            nombre (str): Nombre del empleado
            id (int): Identificador unico del empledado
        """
        self.__nombre = nombre
        self.__id = id
    
    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

class Asistente(Empleado):
    def __init__(self, nombre: str, id: int) -> None:
        super().__init__( nombre, id)
        self.__tipo = "Asistente"
    
    @property 
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def nombre(self, nuevo):
        self.__tipo = nuevo

class Conductor(Empleado):
    def __init__(self, nombre: str, id: int) -> None:
        super().__init__(nombre, id)
        self.__tipo = "Conductor"
    
    @property 
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def nombre(self, nuevo):
        self.__tipo = nuevo