class Turno:
    def __init__(self, conductor:object, asis1:object, asis2:object, camion:object, hora_inicio:str, hora_fin:str, puntos_geograficos:list, recoleccion_Diaria:object) -> None:
        """Constructor de la clase Turno

        Args:
            conductor (object): objeto de tipo empleado que se encarga de conducir el camion
            asis1 (object): objeto de tipo empleado que se encarga de ayudar al conductor
            asis2 (object): objeto de tipo empleado que se encarga de ayudar al conductor
            camion (object): Objeto de tipo camion en el cual se va a realizar la recoleccion
            hora_inicio (str): Hora de inicio del turno
            hora_fin (str): Hora de finalizacion del turno
            puntos_geograficos (list): Lista que guarda los distintos lugares por donde se va a ser la recoleccion, en la lista hay objetos de tipo puntos_geograficos
            recoleccion_Diaria (object): Guarda un objeto de tipo recoleccion_Diaria donde se contabilizara la cantidad de materiales encontrados
            
        """

        self.conductor = conductor
        self.asistente1 = asis1
        self.asistente2 = asis2
        self.camion = camion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.ruta = puntos_geograficos
        self.carga_recogida = 0
        self.recoleccion_Diaria = recoleccion_Diaria

    def recolectar(self)-> None:
        """Metodo para recolectar los materiales en la ruta especifica

        Se itera sobre cada uno de los puntos_geograficos que se encuentran en la lista ruta,
        se accede a el tipo de material que se encuentra en esa lozalización y se contabiliza 
        correspondientente, esta contabilizacion irá guardada en en recoleccion_Diaria que tiene
        un objeto de tipo recoleccion_Diaria se contabiliza el total recogido en carga_recogida
        """

        for i in self.ruta:
            if i.material == "vidrio":
                self.recoleccion_Diaria.cantidad_vidrio += i.cantidad
            elif i.material == "papel":
                self.recoleccion_Diaria.cantidad_papel += i.cantidad
            elif i.material == "plastico":
                self.recoleccion_Diaria.cantidad_plastico += i.cantidad
            elif i.material == "metal":
                self.recoleccion_Diaria.cantidad_metal += i.cantidad
            elif i.material == "residuos organicos":
                self.recoleccion.cantidad_residuos_organicos += i.cantidad
            self.carga_recogida += i.cantidad

    def __repr__(self) -> str:
        """Metodo para representar de forma adecuada el turno
        """
        return f'El turno comenzo a las {self.hora_inicio} y termina a las {self.hora_fin}'