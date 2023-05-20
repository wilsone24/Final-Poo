class puntos_geograficos: 
    def __init__(self, ciudad:str, latitud:int, longitud:int, material:str, cantidad:int) -> None:
        """Clase para crear los diferentes sitios de recogida con el tipo de materialy la cantidad de material

        Args:
            ciudad (str): Nombre de la ciudad donde se encuentra la localizacion
            latitud (int): Latitud de la localizacion
            longitud (int): Longitud de la localizacion
            material (str): Tipo de material que se encuentra en la localizacion
            cantidad (int): Cantidad de material que se encuentra en la localizacion
        """
        self.ciudad = ciudad
        self.latitud = latitud
        self.longitud = longitud
        self.material = material
        self.cantidad = cantidad