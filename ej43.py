from sys import exit
from random import randint
from textwrap import dedent

# Clase principal
class Scene():
    
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

# Clase principal
class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this."
        , "Your Mom would be proud...if she were smarter."
        , "Such a luser."
        , "I have a small puppy that's better at this."
        , "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1 )])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew. You are the last surviving
        memeber and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in the bridge, and
        blow the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons
        Armory when a Gothon jumps out, red scaly skin, dark grimy
        teeth, and evil clown costume flowing around his hate
        filled body. He's blocking the door to the Armory and 
        about to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Tontunas varias
            """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
            Este tío es muy pesado.
            """))
            return 'death'
        
        elif action == "tell a joke":
            print(dedent("""
            Aburrimiento.
            """))
            return 'laser_weapon_armory'
        else:
            print("NO FUNCIONA TÏO")
            return 'central_corridor'
        
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            Es el típico juego...
        """))
        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZED!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                ... que siendo corto se fuerza a que sea largo...
            """))
            return 'the_bridge'
        
        else:
            print(dedent("""
                ... haciendo juego sucio y trucos baratos para liarte.
            """))
            return 'death'
        
class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            Como el maldito juego del caballero.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                ¡Me aburro!
            """))
            return 'Death'
        
        elif action == "slowly place the bomb":
            print(dedent("""
                Qué tostonazo.
            """))
            return 'escape_pod'
        
        else:
            print("NO FUNCIONA")
            return "the_bridge"
        
class EscapePod(Scene):

    def enter():
        print(dedent("""
            Y más texto inútil.
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                Se hace el gracioso ZED con estas tonterías.
            """))
            return 'death'
        
        else:
            print(dedent("""
                Con este ejemplo patético de código
            """))
            return "finished"
        
class Finished(Scene):

    def enter():
        print("You won! Good job.")
        return "finished"
    

# Clase principal
class Map():

    scenes = {
        'central_corridor': CentralCorridor()
        , 'laser_weapon_armory': LaserWeaponArmory()
        , 'the_bridge': TheBridge()
        , 'escape_pod': EscapePod()
        , 'death': Death()
        , 'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
# Punto de entrada
a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()