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
        vesto = Actor('Vesto', 'vesto battle')
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
        
    ####### Classes #######
    
    ### Turn Order ###
    python:
        #Receives combatants and manages who goes next
        class TurnOrder(object):
            
            def __init__(self, spirits, banes):
                self.order = []
                self.actors = {}
                for spirit in spirits:
                    self.actors[spirit.ID] = spirit
                for bane in banes:
                    self.actors[bane.ID] = bane
                
                self.sort()
                    
            # return next actor to go, 
            # actors move to 0 using their speed
            def next(self):
                time = self.actors[self.order[0]].timeTillTurn()
                for key, actor in self.actors.items():
                    actor.nextTurnIn -= time
                
                return self.actors[self.order[0]]
            
            # make a temp value to predict actor turn order
            def sort(self):
                self.order = []
                for key, actor in self.actors.items():
                    added = False
                    for i in range(len(self.order)):
                        if actor.timeTillTurn() < self.actors[self.order[i]].timeTillTurn():
                            self.order.insert(i, key)
                            added = True
                            break
                    if not added:
                        self.order.append(key)
                        
    ### Button ###
    python:
        # Button class to be used in the battle
        class CircleButton(object):
            
            def __init__(self, image):
                # 0 = normal button
                # 1 = hover over button
                # 2 = clicking button
                # 3 = disabled
                self.image = image
                
                self.text = ""
                self.posX = 0
                self.posY = 0
                self.angle1 = angle1
                self.angle2 = angle2
                self.buttonMode = 0
            
            def isOnButton(self, x, y):
                distance = (x - 400)**2 + (y - 400)**2
                if distance >= 10000 and distance <= 40000:
                    angle = math.atan2((y - 400), (x - 400)) * 180 / math.pi
                    return angle > self.angle1 and angle < self.angle2
                return False        