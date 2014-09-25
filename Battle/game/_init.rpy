# Load all assets into game and characters
init:
    $ from string import Template
    
    ####### Scene Images #######

    image office = "assets/office.png"

    ####### Character Images #######
    
    python:
        vesto_path = Template('assets/vesto$expression.png')
        renpy.image('vesto', vesto_path.substitute(expression = ''))
        renpy.image('vesto battle', vesto_path.substitute(expression = '_battle'))
        renpy.image('vesto battle_s', vesto_path.substitute(expression = '_battle_s'))
        
        pers_path = Template('assets/pers$expression.png')
        renpy.image('pers', pers_path.substitute(expression = ''))
        renpy.image('pers battle', pers_path.substitute(expression = '_battle'))
        renpy.image('pers battle_s', pers_path.substitute(expression = '_battle_s'))
        
        logi_path = Template('assets/logi$expression.png')
        renpy.image('logi', logi_path.substitute(expression = ''))
        renpy.image('logi battle', logi_path.substitute(expression = '_battle'))
        renpy.image('logi battle_s', logi_path.substitute(expression = '_battle_s'))
        
        kines_path = Template('assets/kines$expression.png')
        renpy.image('kines', kines_path.substitute(expression = ''))
        renpy.image('kines battle', kines_path.substitute(expression = '_battle'))
        renpy.image('kines battle_s', kines_path.substitute(expression = '_battle_s'))

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

    ####### Variables #######
    
    python:
        spirits = [None, None, None]
        banes = [None, None, None, None, None]
        
    
    ####### Actor Objects #######

    python:
        vesto = Actor('Vesto', 'vesto battle_s')
        pers = Spirit('Pers', 'pers battle_s') # speed = 10
        logi = Spirit('Logi', 'logi battle_s', speed = 13)
        kines = Spirit('Kines', 'kines battle_s', speed = 20, power = 15)

    ####### Bane Objects #######

    python:
        bane = Bane('bob', 'smallBane', speed = 7)
        bob = Bane('jeff', 'boss', speed = 11)

    ####### Key Map Changes #######

    python:
        config.keymap['dismiss'].remove('K_SPACE')
        config.keymap['hide_windows'].append('K_SPACE')
        config.keymap['game_menu'].remove('mouseup_3')
