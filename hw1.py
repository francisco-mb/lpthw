#  Juego de salas y conversación.
#  Crearemos un juego de conversación kink para motivar la programación.
#  Charlas específicas con conversaciones en localizaciones diferentes.

# Salas a representar
# 0 EstateEntrance
# 1 QuietGarden
# 2 LivelyGarden
# 3 DrinkBar
# 4 LodgingRoom

# Entropía personajes
# 0 Mary
# 1 Rachel
# 2 Pink

# Variable global para identificar el número de veces de visitas a cada lugar.
visitas = [0, 0, 0, 0, 0]

# Variable global para controlar la entropía de los personajes
entropia = [0, 0, 0]

def DecisionKO(decision):
    print(f"Not valid option: {decision}. Please, re-type another one.")
    return

def LodgingEntrance():
    """ Id lugar = 0 """
    IdLugar = 0
    visitas[IdLugar] += 1

    if visitas[IdLugar] == 1:
        print("""
        Welcome to this magnificent country house!

        This will be a strange wedding between a nice brazilian guy and an homophobic old friend.

        But your philosophy is not judge people's live, instead to live your life. You have a different MISSION to night, do you?

        """)
    elif visitas[IdLugar] == 2 and entropia[0] == 0 and entropia[1] == 0 and entropia[2] == 0:
        print("""
        You realize that a 40-some year's old lady, with a black dress, high kneels and black hair is searching for a thing inside her clutch. 
        
        After find something very important, unleast for her, rise her eyes and accidentally exchange glances. You keep seeing at she, exchange glances another time
         and then she goes to the LivelyGarden.
        """)

        entropia[0] += 1

    elif entropia[0] > 0 or entropia[1] > 0 or entropia[2]:
        if entropia[0] > entropia[1] and entropia[0] > entropia[2]:
            print("""
            Dear Mary. I found culture interchange between countries very interesting. Brazil and Spain have amazing places to visit, great monuments to admire... like you.
            The first place we can visit is my beautiful room. Is discrete and the bed is quite comfortable. Let me show you the way.
            """)
            
            LodgingRoom(0)

        elif entropia[1] > entropia[0] and entropia[1] > entropia[2]:
            print("""
            Rachel, you have fiancee and y have a wife. It is true. But, where are they? Let me tell you one thing: I like you so much since I saw you at the garden.
            You can chose if to remember this night as a beautiful opportunity not enjoy, or a possibly fantastic sex night with a handful man. What you choose?
            """)

            LodgingRoom(1)

        elif entropia[2] > entropia[0] and entropia[2] > entropia[1]:
            print("""
            Pink, I'm a curious person that asks himself about many things. One of the is blowjobs. Is it true that once gives a gay a try you never go back?
            If you promise to be passive y promise you to feed you with a meat stick and a hot milkshake.
            """)
            LodgingRoom(2)
        else:
            print("""
            Forever alone.
            """)

            LodgingRoom(-1)

    print("Where do you like to go?\n 1.- Quiet Garden \nor\n 2.- Lively Garden\n")

    while True:
        decision = input("> ")

        if decision == "1":
            QuietGarden()
        elif decision == "2":
            LivelyGarden()
        else:
            DecisionKO(decision)
    
def QuietGarden():
    """ ID lugar = 1"""
    IdLugar = 1
    visitas[IdLugar] += 1

    if visitas[IdLugar] == 1:
        print("""
        You are calmly talking with you friends. At your right side a bunch of girls are talking between them. Suddenly one of them starting to speak louder and seeing at you.

        Her name, according to the references of the rest of the group is Rachel. She's a blonde browns eye, probably a 30 and a bit years old girl. She looks an adventurer and brave
        starting to see at you directly. You returns the glance and keep talking to your friends while seeing at her. Skinny body, small breasts, nice face and ass. 

        She moves away while smiling at you. So far so good, you think.
        """)

        entropia[1] += 1

    elif visitas[IdLugar] == 2:
        print("""
        Some people are talking with others, they seem partially drunk. No interesting views to recreat at all.
        """)

    print("Where do you like to go?\n 1.- Estate Entrance \nor\n 2.- Drink Bar\n")

    while True:
        decision = input("> ")

        if decision == "1":
            LodgingEntrance()
        elif decision == "2":
            DrinkBar()
        else:
            DecisionKO(decision)

def LivelyGarden():
    """Id Lugar = 2"""
    IdLugar = 2
    visitas[IdLugar] += 1

    if visitas[IdLugar] == 1:
        print("""
        The guest mafia seems to be right here. Your university's friends are here to, devouring the appetizer. 
        
        You spot several gays acting and making drama around there but one seems to keep your eyes on you. He's young very skinny and have a strange haircut.

        Maybe the night ends in a mission complete, or maybe in a mission failed. In case of the second one, have choices could be a good idea. With all of the precautions,
        checking that your friends are distracted with the food, you see at the pink. Your pose is a typical one, dominant male with wach hand in sight, while the other one is inside the pocket.
        """)

        print("Where do you like to go?\n 1.- Estate Entrance\nor\n 2.- Get closer and start to talk with Pink")

        while True:
            decision = input("> ")

            if decision == "1":
                LodgingEntrance()
            elif decision == "2":
                print("""
                Hi! My name is Francisco. Are you a close friend of the grooms? I am and old friend of the homophobic groom. Where did you get that haircut, it's really nice!
                Maybe you are gym's friends, cause you looks kind of sporty. Let me tell you one thing, make time for meeting with me to talk about the homophobic. We have, many 
                interesting things to say (while exhanging glances). I'm going to Drink Bar.
                """)
                
                entropia[2] += 5

                DrinkBar()

            else:
                DecisionKO(decision)


    elif visitas[IdLugar] == 2:
        print("""
        You have lost all your friends, maybe they move to anoter location. But you no are calmed until have checked that Andrew's wife is not there. GOOD. Rachel starts to get closer.
        When the waiter appears with a new tray with kind of tofu, the opportunity arise.
        """)

        print("Where do you like to go?\n 1.- Estate Entrance\nor\n 2.- Start talking with Rachel or\n 3.- Drink Bar")

        while True:
            decision = input("> ")

            if decision == "1":
                    LodgingEntrance()
            elif decision == "2":
                print("""
                That appetizer seems so healthy. I mean, healthy for you Rachel, because you looks like very sporty. How I knew your name? Well, the first of all I'm Francisco.
                Nice to meet you. I was paying attention at you in the Quiet Garden when your friends say it, true story. Yes, I'm a close friend of the homophobic groom. Really
                agressive and pathetic guy, but intelligent. You are a friend of the Brazilian guy. OK. I'll keep searching my friends. Please, I will see you in a minute.
                """)

                entropia[1] += 5

                DrinkBar()

            elif decision == "3":
                DrinkBar()

            else:
                DecisionKO(decision)
    
    print("Where do you like to go?\n 1.- Estate Entrance \nor\n 2.- Drink Bar\n")

    while True:
        decision = input("> ")

        if decision == "1":
            LodgingEntrance()
        elif decision == "2":
            DrinkBar()
        else:
            DecisionKO(decision)

    
def DrinkBar():
    """ Id lugar = 3"""
    IdLugar = 3
    visitas[IdLugar] += 1

    if visitas[IdLugar] == 1:
        print("""
        Mary the MILF stops next to you and asks for a drink.
        """)

        print("Where do you like to go?\n 1.- Start speaking with Mary\nor\n 2.- Quiet Garden \nor\n 3.- Lively Garden")
        
        while True:
            decision = input("> ")

            if decision == "1":
                print("""
                What drink do you ask for? Really. Do you like alcohol? Me neither. I prefer get lightly drunk instead of get heavily affected. My name is Francisco by the way.
                Are you from Brazil? Really? It's a very interesting country that always wanted to visit. Where do you recommend me to travel? Sao Paulo, Bahía, Brasilia?
                Any of them? You have a deep problem with robery.

                Well stop talking. I wanted to so you places to visit in Spain. Here is very loud, we can go to the entrance to speak more calmly.
                """)

                entropia[0] += 5

                LodgingEntrance()

            elif decision == "2":
                QuietGarden()
            elif decision == "3":
                LivelyGarden()

    else:
        print("""
        Any interesting pussy here. You should move before the twelve chimes.
        """)

        print("Where do you like to go?\n 1.- Quiet Garden \nor\n 2.- Lively Garden\n")

        while True:
            decision = input("> ")

            if decision == "1":
                QuietGarden()
            elif decision == "2":
                LivelyGarden()
            else:
                DecisionKO(decision)

def LodgingRoom(personaje):
    if personaje == -1:
        print("""
        Do not change nothing of your life.
        """)

    elif personaje == 0:
        print("""
        Slow, hard and sweet. Never a Toledo night reach a hot temperature in the early days of november.
        """)
    
    elif personaje == 1:
        print("""
        Hard and kinky. Hard as streetlamp, and like a demolition man. I'd discover how I like skinny girls.
        """)

    elif personaje == 2:
        print("""
        All your friends, the grooms and even your wife knows the truth: gay-fucker. Only one thing to say:
        Blowjobs are fantastic made by a gay.
        """)

    exit(0)

LodgingEntrance()

exit(0)