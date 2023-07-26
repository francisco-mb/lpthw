class Sala():

    # Variables globales
    SalasSiguientes : list
    SalaAnterior : str # tiene que estar en la lista de siguientes
    AccionesSala : list
    NumVisitas = 0
    ObjetosRecogidos : list

    def Explorar(self, SalaAnterior : str):
        exit(1)

    def CalcularSalida(self
                        , SalaSiguiente : str
                        , Objeto : str) -> str:
        return f"{SalaSiguiente}|{Objeto}"


class Pasillo(Sala):

    SalasSiguientes = [
        'salón'
        , 'baño'
        , 'estudio'
        , 'cocina'
        , 'pasillo'
    ]

    AccionesSala = [
        'echar un vistazo'
        , 'coger'
        , 'ir a otra sala'
    ]

    def Explorar(
            self
            , SalaAnteriorEnt : str
            , MochilaObjetos : list[str]) -> str:
        
        self.SalaAnterior = SalaAnteriorEnt
        self.ObjetosRecogidos = MochilaObjetos
        self.NumVisitas += 1

        if Pasillo.NumVisitas == 1:
            print("Ya estás en casita. ¡Tenemos que buscar a Fran!\nTiene que ir al colegio.")

        print("Te encuentras en el pasillo, puedes hacer lo siguiente:\n")
        accionId = 0
        for accion in Pasillo.AccionesSala:
            print(f"{accionId}.- {accion}\n")
            accionId += 1

        print("¿Qué opción escoges?")
        accionId = int(input("> "))

        if accionId >= len(Pasillo.AccionesSala):
            print("Código de acción desconocido.")
            Pasillo.Explorar(Pasillo.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 0:
            print(f"Te pones a {Pasillo.AccionesSala[accionId]} y no ves nada.")

        elif accionId == 1:
            print(f"Quieres {Pasillo.AccionesSala[accionId]} algo, pero no hay nada que recoger.")

        print("Desde el pasillo puedes ir a la salas siguientes:")
        salaId = 0
        for sala in Pasillo.SalasSiguientes:
            print(f"{salaId}.- {sala}\n")
            salaId += 1


        print("¿Qué sala escoges?")
        salaId = int(input("> "))
        
        if salaId == len(Pasillo.SalasSiguientes):
            print("Volvemos a la sala anterior.")
            self.Explorar(self.SalaAnterior, self.ObjetosRecogidos)

        else:
            try:
                return self.CalcularSalida('pasillo', self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida('pasillo', "")
        
        # Nunca se alcanzará este punto
        exit(1)

class Salón(Sala):
    SalasSiguientes = [
        'baño'
    ]

    AccionesSala = [
        'echar un vistazo'
        , 'coger'
        , 'ir a otra sala'
    ]

    def Explorar(
            self
            , SalaAnteriorEnt : str
            , MochilaObjetos : list[str]) -> str:
        self.SalaAnterior = SalaAnteriorEnt
        self.ObjetosRecogidos = MochilaObjetos
        self.NumVisitas += 1

        if Salón.NumVisitas == 1:
            print("Bienvenido al Salón, camarada. ¿Esperas encontrar algo bueno?\n")

        print("\n¿Qué deseas hacer amo?")
        accionId = 0
        for accion in Salón.AccionesSala:
            print(f"{accionId}.- {accion}\n")
            accionId += 1

        print("¿Qué acción escoges?")
        accionId = int(input("> "))

        if accionId >= len(Salón.AccionesSala):
            print("Código de sala desconocido")
            self.Explorar(Salón.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 0:
            print("El furgón era oscuro, y el salón está en penumbra.")
            if len(self.ObjetosRecogidos) == 0:
                print("Sin embargo, hay una curiosa llave de LEGO encima del sofá...\n")

            self.Explorar(self.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 1 and len(self.ObjetosRecogidos) == 0:
            print("Esta llave tiene que abrir algo interesante en alugna parte, ¡nos la guardamos en la mochila!\n")
            self.ObjetosRecogidos[0] = 'llave'

        print("Desde el salón puedes ir a las siguientes salas:")
        salaId = 0
        for sala in Salón.SalasSiguientes:
            print(f"{salaId}.- {sala}")
            salaId += 1

        print("¿Qué sala escoges?")
        salaId = int(input("> "))

        if salaId > len(self.SalasSiguientes):
            print("Código de sala desconocido.")
            self.Explorar(SalaAnteriorEnt, self.ObjetosRecogidos)

        elif salaId == len(self.SalasSiguientes):
            print("Volviendo a la sala anterior")
            try:
                return self.CalcularSalida(self.SalaAnterior, self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida(self.SalaAnterior, "")

        else:
            try:
                return self.CalcularSalida(self.SalasSiguientes[salaId], self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida(self.SalasSiguientes[salaId], "")
        
class Estudio(Sala):
    SalasSiguientes = [
        'cocina'
    ]

    AccionesSala = [
        'echar un vistazo'
        , 'llamar por telefono'
        , 'ir a otra sala'
    ]

    def Explorar(
            self
            , SalaAnteriorEnt : str
            , MochilaObjetos : list[str]) -> str:
        self.SalaAnterior = SalaAnteriorEnt
        self.ObjetosRecogidos = MochilaObjetos
        self.NumVisitas += 1

        if self.NumVisitas == 1:
            print("Bienvenido al Estudio, Templo de Fran padre. Tenemos ordenador, teléfono y otras cositas.\n")

        print("\n¿Qué quieres hacer?")
        accionId = 0
        for accion in self.AccionesSala:
            print(f"{accionId}.- {accion}\n")
            accionId += 1

        print("¿Qué acción escoges?")
        accionId = int(input("> "))

        if accionId >= len(self.AccionesSala):
            print("Código de sala desconocido")
            self.Explorar(self.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 0:
            print("Miras debajo de la mesa a ver si está Fran... pero no encuentras nada\n")

            self.Explorar(self.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 1:
            print("Llamas por teléfono a Consuelo. Le recuerdas que su empanada está deliciosa.\n")

        print("Desde el estudio puedes ir a las siguientes salas:")
        salaId = 0
        for sala in self.SalasSiguientes:
            print(f"{salaId}.- {sala}")
            salaId += 1

        # Sala anterior
        print(f"{salaId}.- {self.SalaAnterior}")

        print("¿Qué sala escoges?")
        salaId = int(input("> "))

        if salaId == len(self.SalasSiguientes):
            print("Volviendo a la sala anterior.")
            try:
                return self.CalcularSalida(self.SalaAnterior, self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida(self.SalaAnterior, "")
        
        elif salaId > len(self.SalasSiguientes):
            print("Código de sala incorrecto.")
            self.Explorar(SalaAnteriorEnt, self.ObjetosRecogidos)

        else:
            try:
                return self.CalcularSalida(self.SalasSiguientes[salaId], self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida(self.SalasSiguientes[salaId], "")
        
class Cocina(Sala):
    SalasSiguientes = [
        ''
    ]

    AccionesSala = [
        'echar un vistazo'
        , 'abrir cofre'
    ]

    def Explorar(
            self
            , SalaAnteriorEnt : str
            , MochilaObjetos : list[str]):
        self.SalaAnterior = SalaAnteriorEnt
        self.ObjetosRecogidos = MochilaObjetos
        self.NumVisitas += 1

        if self.NumVisitas == 1:
            print("Bienvenido a la cocina.\n")

        print("\n¿Qué quieres hacer?")
        accionId = 0
        for accion in self.AccionesSala:
            print(f"{accionId}.- {accion}\n")
            accionId += 1

        print("¿Qué acción escoges?")
        accionId = int(input("> "))

        if accionId >= len(self.AccionesSala):
            print("Código de acción desconocido")
            self.Explorar(self.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 0:
            print("Ves que hay un cofre de MINECRAFT bien grande en el centro.\n")

            self.Explorar(self.SalaAnterior, self.ObjetosRecogidos)

        elif accionId == 1 and self.ObjetosRecogidos[0] == 'llave':
            print("¡Has encontrado a Fran. Fin del juego.!\n")
            exit(1)

        elif accionId == 1 and self.ObjetosRecogidos[0] != 'llave':
            print("No puedes abrirlo, te falta una llave con forma de LEGO.\n")

        print("Desde la cocina puedes ir a las siguientes salas:")
        salaId = 0
        for sala in self.SalasSiguientes:
            print(f"{salaId}.- {sala}")
            salaId += 1

        # Sala anterior
        print(f"{salaId}.- {self.SalaAnterior}")

        print("¿Qué sala escoges?")
        salaId = int(input("> "))

        if salaId == len(self.SalasSiguientes):
            print("Volviendo a la sala anterior.")
            try:
                return self.CalcularSalida(self.SalaAnterior, self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida(self.SalaAnterior, "")
        
        elif salaId > len(self.SalasSiguientes):
            print("Código de sala incorrecto.")
            self.Explorar(SalaAnteriorEnt, self.ObjetosRecogidos)

        else:
            try:
                return self.CalcularSalida(self.SalasSiguientes[salaId], self.ObjetosRecogidos[0])
            except IndexError:
                return self.CalcularSalida(self.SalasSiguientes[salaId], "")


# prueba = Cocina()
# MochilaObjetos = [""]
# prueba.Explorar('pasillo', MochilaObjetos)

# class Salón(Sala):
#     SalaSiguiente = 'baño'
#     SalaAnterior = 'pasillo'
#     Respuesta : str = ''
#     ContadorVisitas : int = 0

#     def Entrar():
#         if Salón.ContadorVisitas == 0:
#             Salón.ContadorVisitas += 1
#             print("En el salón. Fran... Fran, ¿dónde estás?")
#             print("Aquí no hay nada, vamos a la siguiente habitación ¿S/N?")

#         else:
#             print("Salón ya visitado antes, no parece que esté Fran. ¿Quieres ir a la siguiente habitación (S/N)?")

#         # Recoge la respuesta de ambas preguntas.
#         Salón.Respuesta = str(input('> '))            

#         if Salón.Respuesta == 'S':
#             return Salón.GetSalaSiguiente()
#         else:
#             Salón.Entrar()
        
#     def GetSalaAnterior():
#         return Salón.SalaSiguiente
    
#     def GetSalaAnterior():
#         return Salón.SalaAnterior
    

# class Baño(Sala ):
#     SalaSiguiente : str = 'estudio'
#     SalaAnterior : str = 'salón'
#     Respuesta : str = ''
#     ContadorVisitas : int = 0

#     def Entrar():
#         if Baño.ContadorVisitas == 0:
#             Baño.Contador += 1
#             print("Aquí hay muchísima humedad, parece que alguien no quiere ventilar nunca.")
#             print("Fran no está detrás de la puerta, ni está en la bañera escondido.")
#             print("Este chico es un traviesillo. ¿Buscamos en la siguiente habitación, o volvemos a la anterior? (S/N).")

#         else:
#             Baño.Respuesta = str(input('> '))


# class Estudio(Sala):

# class Cocina(Sala):

# class Tendedero(Sala):