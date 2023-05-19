class recoleccion_Diaria:
    def __init__(self, empresa:object) -> None:
        """Constructor de la clase recoleccion diaria
        Se inicializan las variables que contabilizaran la cantidad de materiales recogidos

        Args:
            empresa (object): Objeto de tipo empresa para guardar la contabilizacion de la recoleccion diaria
        """
        self.empresa = empresa
        self.cantidad_vidrio = 0
        self.cantidad_papel = 0
        self.cantidad_plastico = 0
        self.cantidad_metal = 0
        self.cantidad_residuos_organicos = 0

    def get_Residuos_Obtenidos(self)-> None:
        """Metodo para poder visualizar la recoleccion diaria en la ruta especifica.
        
        Se itera sobre cada uno de los materiales para visualizar la cantidad de cada uno de ellos
        """
        print('----------------------------------------')
        print(f'La empresa {self.empresa.nombre} recolectó:')
        print('----------------------------------------')
        print('|   Material    |    Cantidad    |')
        print('----------------------------------------')
        print(f'|    Vidrio     |   {self.cantidad_vidrio}    |')
        print('----------------------------------------')
        print(f'|    Papel      |   {self.cantidad_papel}    |')
        print('----------------------------------------')
        print(f'|   Plástico    |   {self.cantidad_plastico}    |')
        print('----------------------------------------')
        print(f'|     Metal     |   {self.cantidad_metal}    |')
        print('----------------------------------------')
        print(f'| Residuos org. |   {self.cantidad_residuos_organicos}    |')
        print('----------------------------------------')