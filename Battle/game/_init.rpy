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

        smallBane_path = Template('assets/bane_shitling$expression.png')
        for i in range(5):
            renpy.image('smallBane' + str(i), smallBane_path.substitute(expression = ''))
            renpy.image('smallBane' + str(i) + ' battle', smallBane_path.substitute(expression = '_icon'))
            renpy.image('smallBane' + str(i) + ' battle_s', smallBane_path.substitute(expression = '_battle_s'))
        
        boss_path = Template('assets/bane_boss$expression.png')
        renpy.image('boss', boss_path.substitute(expression = ''))
        renpy.image('boss battle', boss_path.substitute(expression = '_icon'))
        renpy.image('boss battle_s', boss_path.substitute(expression = '_battle_s'))

    #image smallBane = "assets/bane_shitling.png"
    #image boss = "assets/bane_boss.png"

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
        vesto = Actor('Vesto', 'vesto')
        pers = Spirit('Pers', 'pers') # speed = 10
        logi = Spirit('Logi', 'logi', speed = 13)
        kines = Spirit('Kines', 'kines', speed = 20, power = 15)

    ####### Bane Objects #######

    python:
        bane = []
        for i in range(5):
            bane.append(Bane('bob' + str(i), 'smallBane' + str(i), speed = 7))
        bob = Bane('jeff', 'boss', speed = 11)

    ####### Key Map Changes #######

    python:
        config.keymap['dismiss'].remove('K_SPACE')
        config.keymap['hide_windows'].append('K_SPACE')
        config.keymap['game_menu'].remove('mouseup_3')
