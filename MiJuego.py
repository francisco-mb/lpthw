from MiJuego_Motor import Motor
from MiJuego_Mapa import Mapa

MapaInicial = Mapa("pasillo")
print(Mapa.SalaInicio)
EntidadMotor = Motor(MapaInicial)

EntidadMotor.Jugar()