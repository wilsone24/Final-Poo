class puntos_geograficos: 
    def __init__(self, latitud:int, longitud:int, material:str, cantidad:int) -> None:
        """Clase para crear los diferentes sitios de recogida con el tipo de materialy la cantidad de material

        Args:
            latitud (int): _description_
            longitud (int): _description_
            material (str): _description_
            cantidad (int): _description_
        """
        self.latitud = latitud
        self.longitud = longitud
        self.material = material
        self.cantidad = cantidad