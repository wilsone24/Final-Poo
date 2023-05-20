class Empleado:
    def __init__(self, nombre:str, id:int) -> None:
        """Constructor de la clase Empleado

        Args:
            tipo (str): Tipo de empleado
            nombre (str): Nombre del empleado
            id (int): Identificador unico del empledado
        """
        self.__nombre = nombre
        self.id = id
    
    @property 
    def nombre(self)->str:
        """Funcion para acceder al nombre del empleado

        Returns:
            str: Nombre del empleado
        """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo:str)->None:
        """Funcion para definir un nuevo nombre para el empleado

        Args:
            nuevo (str): Nuevo nombre del empleado
        """
        self.__nombre = nuevo


class Asistente(Empleado):
    def __init__(self, nombre: str, id: int) -> None:
        """Crear un empleado de tipo asistente

        Args:
            nombre (str): Nombre del empleado
            id (int): Identificador Unico
        """
        super().__init__( nombre, id)
        self.__tipo = "Asistente"
    
    @property 
    def tipo(self):
        """Funcion para acceeder al tipo de empleado

        Returns:
            str: tipo de empleado
        """
        return self.__tipo
    
    @tipo.setter
    def tipo(self, nuevo:str)->None:
        """Definie un nuevo tipo de empleado

        Args:
            nuevo (str): nuevo tipo de empleado
        """
        self.__tipo = nuevo

    def Tarea(self):
        print(f'El Asistente {self.nombre} #{self.id} Recolecta')

class Conductor(Empleado):
    def __init__(self, nombre: str, id: int) -> None:
        super().__init__(nombre, id)
        self.__tipo = "Conductor"
    
    @property 
    def tipo(self):
        """Funcion para acceeder al tipo de empleado

        Returns:
            str: tipo de empleado
        """
        return self.__tipo
    
    def Tarea(self):
        print(f'El conductor {self.nombre} esta conduciendo')
    
    @tipo.setter
    def tipo(self, nuevo:str):
        """Definie un nuevo tipo de empleado

        Args:
            str: nuevo tipo de empleado
        """
        self.__tipo = nuevo