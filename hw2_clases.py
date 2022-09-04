"""Definición general de las clases a utilizar en el juego conversacional Toledo's Adventure."""

class Habitacion(object):
    """Representa cada lugar visitable del mapa.
    
    Características a destacar:
        - Desde aquí nos moveremos a otras habitaciones o realizaremos otras acciones.
    
        - Según el número de visitas, podremos hacer unas cosas u otras.
    """

    def __init__(self, nombreHabitacion: str):
        self.numVisitas: int = 0
        self.nombreHabitacion: str = nombreHabitacion

    def DeUnVistazo(self):
        pass

    def Accion(self, opcion: int):
        pass


class Personajes(object):
    """Representa alguien con quien interactuar.

    Características a destacar:
        - Varias líneas de diálogo, dependiendo de cuantas veces hemos hablado anteriormente.

        - Podrá cambiar de habitación tras interactuar.
    """

    def __init__(self, nombre: str, habitacion: int):
        self.nombre = nombre
        self.entropia = 0
        self.habitacion = habitacion


class Mapa(object):
    """Contenedor ordenado de habitaciones.
    
    Su estructura definirá el juego. Las habitaciones solo se conectarán entre sí como si fueran una doble lista enlazada.
    
    Contendrá una referencia a la habitación inicial.
    """

    def __init__(self):
        pass


class Motor(object):
    """Punto de inicio del juego.
    
    Cargará unas habitaciones y personajes diferentes por juego, arrancará el mismo, y gestionará la situación del jugador.
    """

    def __init__(self):
        pass

    

