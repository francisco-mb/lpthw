from MiJuego_Salas import Pasillo, Salón, Estudio, Cocina
from MiJuego_Mapa import Mapa

class Motor():

    SalaInicio = ""
    Mochila = [""]

    def __init__ (self, Mapa):
        self.MapaJuego = Mapa

    def Jugar(self):
        SalaActual = self.MapaJuego.SalaInicio
        ObjetoMochila = ""

        while SalaActual != "cocina":
            resultado = Mapa.habitaciones[SalaActual].Explorar(SalaActual, ObjetoMochila)
            SalaAnterior = resultado.split("|")[0]
            ObjetoMochila = resultado.split("|")[1]
            self.Mochila.append(ObjetoMochila)

            # Siguiente sala
            SalaActual = self.MapaJuego.SiguienteSala(SalaAnterior)

        # Alcanzada la última sala, entramos
        Mapa.habitaciones[SalaActual].Explorar(SalaActual, self.Mochila)