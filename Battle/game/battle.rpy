init:
    
    $ import math
    #$ import Button
    
    # Positions
    python:        
        
        leaderSpot = Position(xalign=.01, yalign=.5)
        
        partySpots = [Position(xalign=.3, yalign=.5), 
            Position(xalign=.25, yalign=.1), 
            Position(xalign=.25, yalign=.9)]

        enemySpots = [Position(xalign=.7, yalign=.5),
            Position(xalign=.7, yalign=.05),
            Position(xalign=.7, yalign=.95),
            Position(xalign=.9, yalign=.7),
            Position(xalign=.9, yalign=.3)]
        
        #boss at spot 0
        enemyBossSpots = [Position(xalign=.95, yalign=.5),
            Position(xalign=.65, yalign=.5),
            Position(xalign=.7, yalign=.1),
            Position(xalign=.7, yalign=.9)]
        
    # Class and displayable to decide which attack to use of a spirit
    python:
        
        class Attack(renpy.Displayable):
            
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                # temp button location
                self.xpos = 200
                self.ypos = 200
                
                self.cursorx = 0
                self.cursory = 0
                
                self.turnOver = False
                self.skill = 'attack'
                
                # 0 = normal button
                # 1 = hover over button
                # 2 = clicking button
                self.button = [Image("assets/selectRing/TopLeftCircle.png"), 
                    Image("assets/selectRing/TopLeftCircleHover.png"), 
                    Image("assets/selectRing/TopLeft.png")]
                self.buttonMode = 0
                self.mouseDown = False
                self.buttonPressing = None
            
            # return if cursor is on button
            def isOnButton(self, x, y, angle1, angle2):
                distance = (x - 400)**2 + (y - 400)**2
                if distance >= 10000 and distance <= 40000:
                    angle = math.atan2((y - 400), (x - 400)) * 180 / math.pi
                    return angle > angle1 and angle < angle2
                return False
                            
            # rendering cycle
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)
                
                # button
                pi = renpy.render(self.button[self.buttonMode], 200, 200, st, at)
                r.blit(pi, (self.xpos, self.ypos))
                
                # cursor text, display coords
                text = Text(_("(" + str(self.cursorx) + ", " + str(self.cursory) + ")"), size=24, color="#ffffff")
                cursor = renpy.render(text, 800, 600, st, at)
                r.blit(cursor, (self.cursorx, self.cursory))
                
                # display outlined text on button, centered
                spirit1Skill1Text = Text(_("PUNCH"), xanchor = 0.5, font = 'impact.ttf',
                    antialias = True, size = 24, color = "#ffffff", outlines = [(4, "#000000", 0, 0)])
                spirit1Skill1 = renpy.render(spirit1Skill1Text, 500, 500, st, at)
                r.blit(spirit1Skill1, (267 - spirit1Skill1.width / 2, 264))
                
                renpy.redraw(self, 0)
                    
                return r
            
            # events
            def event(self, ev, x, y, st):
                
                import pygame
                
                # Release mouse, trigger button press
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    self.mouseDown = False
                    if self.isOnButton(x, y, -180, -90):
                        self.turnOver = True
                    
                # Mouse movement
                if ev.type == pygame.MOUSEMOTION:
                    self.cursorx = x
                    self.cursory = y
                    
                # position over button
                if self.isOnButton(x, y, -180, -90):
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                        self.mouseDown = True
                    if self.mouseDown: 
                        self.buttonMode = 2
                    else: 
                        self.buttonMode = 1
                else:
                    self.buttonMode = 0

                # end render cycle
                if self.turnOver:
                    return self.skill
                else:
                    raise renpy.IgnoreEvent()
    
    # After selecting an attack, class for choosing a target
    python:
        
        class Target(renpy.Displayable):
            
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                self.arrow = Image("assets/x.png")
                
                self.bane1 = True
                self.selected = None
                self.target = False
                
                self.cursorx = 0
                self.cursory = 0
                
                self.bane1xpos = 810
                self.bane1ypos = 380
                
                self.bane2xpos = 880
                self.bane2ypos = 160
                self.turnOver = None
                
                self.buttonMode = 0
                self.mouseDown = False
            
            # return if cursor is in elliptical area
            def isInArea(self, x, y, h, k, rx, ry):
                return (( ((x - h)**2) / rx**2 ) + ( ((y - k)**2) / ry**2 )) <= 1
                            
            # rendering cycle
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                if self.target:
                    pi = renpy.render(self.arrow, 200, 200, st, at)
                    r.blit(pi, (self.bane1xpos if self.bane1 else self.bane2xpos, 
                        self.bane1ypos if self.bane1 else self.bane2ypos))
                
                text = Text(_("(" + str(self.cursorx) + ", " + str(self.cursory) + ")"), size=24, color="#ffffff")
                cursor = renpy.render(text, 800, 600, st, at)
                r.blit(cursor, (self.cursorx, self.cursory))
                
                renpy.redraw(self, 0)
                    
                return r
            
            # Handles events.
            def event(self, ev, x, y, st):
                
                import pygame
                
                # Cancel attack
                if (ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE) or (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3):
                    return False

                # Mouse move
                if ev.type == pygame.MOUSEMOTION:
                    self.cursorx = x
                    self.cursory = y
                    # over a target
                    if self.isInArea(x, y, self.bane1xpos, self.bane1ypos, 50, 50):
                        self.bane1 = True
                        self.target = True
                        self.selected = "bane1"
                    elif self.isInArea(x, y, self.bane2xpos, self.bane2ypos, 50, 50):
                        self.bane1 = False
                        self.target = True
                        self.selected = "bane2"
                
                # Release mouse, trigger button press
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    if self.target:
                        self.turnOver = True

                # end render cycle
                if self.turnOver:
                    return self.selected
                else:
                    raise renpy.IgnoreEvent()

label battle(leader = vesto, party = spirits, bossBattle = False, enemies = banes):
    
    #hide dialogue box
    window hide None
    # disable saving
    $ _game_menu_screen = None

    python:
        # place party members
        if leader:
            renpy.show(leader.img, at_list = [leaderSpot])
        for i in range(len(party)):
            if party[i]:
                renpy.show(party[i].img, at_list = [partySpots[i]])
    
        # place enemies
        for i in range(len(enemies)):
            if enemies[i]:
                renpy.show(enemies[i].img, at_list = [enemyBossSpots[i] if bossBattle else enemySpots[i]])
                
    
#        if party[0]:
#            renpy.show(party[0].img, at_list = [partySpots[0]])
#        if party[1]:
#            renpy.show(party[1].img, at_list = [partySpots[1]])
#        if party[2]:
#            renpy.show(party[2].img, at_list = [partySpots[2]])

#    if bossBattle:
#        show smallBane at enemyBossSpots[0]
#        #show bane2 at enemyBossSpots[1] 
#        #show bane3 at enemyBossSpots[2] 
#        show boss at boss
#    else:
#        show bane1 at enemySpots[0] 
#        show bane2 at enemySpots[1] 
#        show bane3 at enemySpots[2] 
#        show bane4 at enemySpots[3] 
#        show bane5 at enemySpots[4]

    
#    python:
#        def clicky():
#            renpy.sound.play('assets/smw_1-up.wav')
        
#        ui.imagebutton(Image('Mario-icon.png')
#            , im.MatrixColor(Image('Mario-icon.png'), im.matrix.invert())
#            , Image('Mario-icon.png')
#            , clicked = clicky)
    

    python:
        noTarget = True
        while noTarget:
            ui.add(Attack())
            attack = ui.interact()
            
            ui.add(Target())
            target = ui.interact()
            
            if target:
                _return = attack + " " + target
                noTarget = False
                
        
    $ _game_menu_screen = "save_screen"
    return _return