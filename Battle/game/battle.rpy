init:
    
    $ import math
    #$ import Button
    
    # Positions
    python:        
        
        leaderSpot = Position(xalign=0.00, yalign=-0.03)
        
        partySpots = [Position(xalign=0.02, yalign=0.33), 
            Position(xalign=0.02, yalign=0.60), 
            Position(xalign=0.02, yalign=0.87)]

        bossSpot = Position(xalign=1.0, yalign=-0.03)
        
        enemySpots = [Position(xalign=0.98, yalign=0.30),
            Position(xalign=0.98, yalign=0.4625),
            Position(xalign=0.98, yalign=0.625),
            Position(xalign=0.98, yalign=0.7875),
            Position(xalign=0.98, yalign=0.95)]
        
    # Class and displayable to decide which attack to use of a spirit
    python:
        
        class Attack(renpy.Displayable):
            
            def __init__(self, spirit):
                renpy.Displayable.__init__(self)
                
                self.buttons = [Button(550, 255), # Attack button
                    #self.attackButton.icon = spirit.attack.icon
                    
                    Button(490, 110), # Skill 1 button
                    #self.skill1Button.icon = spirit.skill1.icon

                    Button(490, 420), # Skill 2 button
                    #self.skill2Button.icon = spirit.skill2.icon
                    
                    Button(610, 190), # Combo Skill 1 button
                    #self.comboSkill1Button.icon = spirit.combo1.icon
                    
                    Button(610, 340), # Combo Skill 2 button
                    #self.comboSkil12Button.icon = spirit.combo2.icon
                    
                    Button(240, 110)] # Defend button
                    #self.defendIcon = #defend icon

                # cursor location
                self.cursorx = 0
                self.cursory = 0
                
                # skill used
                self.skill = None

                self.buttonPressing = None
            
            # rendering cycle
            def render(self, width, height, st, at):
                
                # select skill if none selected
                if not self.skill:
                    # The Render object we'll be drawing into.
                    r = renpy.Render(width, height)
                    
                    # buttons
                    for button in self.buttons:
                        if button.visible:
                            b = renpy.render(button.getImage(), 75, 75, st, at)
                            r.blit(b, (button.posX, button.posY))
                
                # choose target after skill selection
                else:
                    pass
                    
                # cursor text, display coords
                text = Text(_("(" + str(self.cursorx) + ", " + str(self.cursory) + ")"), size=24, color="#ffffff")
                cursor = renpy.render(text, 800, 600, st, at)
                r.blit(cursor, (self.cursorx, self.cursory))
                
                renpy.redraw(self, 0)
                    
                return r
            
            # events
            def event(self, ev, x, y, st):
                
                import pygame
                
                if not self.skill:
                    # Release mouse, trigger button press
                    if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                        if self.buttonPressing:
                            if self.buttonPressing.isOnButton(x, y):
                                self.skill = self.buttons.index(self.buttonPressing)
                            self.buttonPressing = None
                        
                    # position over button
                    for button in self.buttons:
                        if button.isOnButton(x, y):
                            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                                self.buttonPressing = button
                            if self.buttonPressing == button: 
                                button.buttonMode = 2
                            else: 
                                button.buttonMode = 1
                        else:
                            button.buttonMode = 0
                
                # Mouse movement
                if ev.type == pygame.MOUSEMOTION:
                    self.cursorx = x
                    self.cursory = y

                # end render cycle
                if self.skill:
                    return {
                        0 : 'attack',
                        1 : 'skill1',
                        2 : 'skill2',
                        3 : 'combo1',
                        4 : 'combo2',
                        5 : 'defend'
                        } [self.skill]
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

label battle(leader = vesto, party = spirits, boss = None, enemies = banes):
    
    #hide dialogue box
    window hide None
    # disable saving
    $ _game_menu_screen = None

    python:
        # place party members
        if leader:
            renpy.show(leader.img + ' battle_s', at_list = [leaderSpot])
        for i in range(len(party)):
            if party[i]:
                renpy.show(party[i].img + ' battle_s', at_list = [partySpots[i]])
    
        # place enemies
        if boss:
            renpy.show(boss.img + ' battle_s', at_list = [bossSpot])
        for i in range(len(enemies)):
            if enemies[i]:
                renpy.show(enemies[i].img + ' battle_s', at_list = [enemySpots[i]])

    

    python:
        noTarget = True
        while noTarget:
            ui.add(Attack(party[0]))
            attack = ui.interact()
            
            ui.add(Target())
            target = ui.interact()
            
            if target:
                _return = attack + " " + target
                noTarget = False
                
        
    $ _game_menu_screen = "save_screen"
    return _return