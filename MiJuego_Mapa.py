from MiJuego_Salas import Pasillo, Salón, Estudio, Cocina

class Mapa():
    habitaciones = {
        "pasillo" : Pasillo()
        , "salón" : Salón()
        , "estudio" : Estudio()
        , "cocina" : Cocina()
    }

    SalaInicio = ""

    def __init__(self, SalaInicio : str) -> None:
        self.SalaInicio = SalaInicio

    def SiguienteSala (self, SalaActual): 
        temp = list(self.habitaciones)
        
        try:
            return temp[temp.index(SalaActual) + 1]
        except (ValueError, IndexError):
            return None
