class Camion:
    def __init__(self, placa:str, modelo:str) -> None:
        """Metodo constructor para generar los distintos camiones

        Args:
            placa (str): Placa asignada al camion, identificador unico
            modelo (str): modelo del camion
        """
        self.__placa = placa
        self.modelo = modelo
    
    @property 
    def placa(self)->str:
        """Funcion para acceder a la placa del camion

        Returns:
            str: Placa del camion
        """
        return self.__placa
    
    @placa.setter
    def nombre(self, nuevo:str)->None:
        """Funcion para definir una nueva placa para el camion

        Args:
            nuevo (str): Nueva placa del camion
        """
        self.__placa = nuevo