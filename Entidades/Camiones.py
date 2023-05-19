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
    def placa(self):
        return self.__placa
    
    @placa.setter
    def nombre(self, nuevo):
        self.__placa = nuevo