init:
    $ import Actor
    # Load all assets into game and characters
    ####### Scene Images #######

    image office = "assets/office.png"

    ####### Character Images #######

    image vesto = "assets/vesto.png"
    image pers = "assets/pers_battle.png"
    image logi = "assets/logi_battle.png"
    image kines = "assets/kines_battle.png"

    image smallBane = "assets/bane_shitling.png"
    image boss = "assets/bane_boss.png"

    ####### Sprites #######



    ####### Music #######



    ####### Sounds #######



    ####### Misc. Images #######



    ####### Characters #######

    define v = Character('Vesto')
    define p = Character('Pers')
    define l = Character('Logi')
    define k = Character('Kines')

    ####### Actor Objects #######

    python:
        pers = Actor.Spirit('Pers', 'pers') # speed = 10
        logi = Actor.Spirit('Logi', 'logi', speed = 13)
        kines = Actor.Spirit('Kines', 'kines', speed = 20, power = 15)

    ####### Bane Objects #######

    python:
        bane = Actor.Bane('bob', 'smallBane', speed = 7)
        bob = Actor.Bane('jeff', 'boss', speed = 11)

    ####### Key Map Changes #######

    python:
        #config.keymap['dismiss'].remove('K_SPACE')
        #config.keymap['hide_windows'].append('K_SPACE')
        pass