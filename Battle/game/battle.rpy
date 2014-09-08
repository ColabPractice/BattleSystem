init:
    
    python:
        import Actor
        import math

    #ATL Section
#    transform shake(times):
#        parallel:
#            im.Scale("assets/ShadowBoss.png", 400, 600)
        
#        parallel:
#            linear .01 xoffset (10)
#            linear .01 xoffset (-10)
#            linear .01 xoffset (10)
#            linear .01 xoffset (-10)
#            linear .01 xoffset (0)
#            repeat times
            
        
    #show InsertNameHere at shake(InsertHowManyTimes)
    
    python:
        cPers = Actor.Spirit("Pers", "pers")
        cKines = Actor.Spirit("Kines", "kines", speed = 20, power = 15)
        cLogi = Actor.Spirit("Logi", "logi", speed = 5, power = 40)
    
    python:
        
        renpy.image("spirit1", im.Scale("assets/cPers.png", 180, 200))
        renpy.image("spirit2", im.Scale("assets/cPers.png", 180, 200))
        renpy.image("spirit3", im.Scale("assets/cPers.png", 180, 200))
        
        renpy.image("bane1", im.Scale("assets/weakhearth.png", 150, 150))
        renpy.image("bane2", im.Scale("assets/weakhearth.png", 150, 150))
        renpy.image("bane3", im.Scale("assets/weakhearth.png", 150, 150))
        renpy.image("bane4", im.Scale("assets/weakhearth.png", 150, 150))
        renpy.image("bane5", im.Scale("assets/weakhearth.png", 150, 150))
        
        renpy.image("boss", im.Scale("assets/ShadowBoss.png", 400, 600))
        
        renpy.image("vesto", im.Scale("assets/cVesto.png", 230, 300))

        # TODO temp positions done, tweak them after final images are done
        vestoSpot = Position(xpos=.01, xanchor=.01, ypos=.5, yanchor=.5)
        
        spirit1Spot = Position(xpos=.3, xanchor=.3, ypos=.5, yanchor=.5)
        spirit2Spot = Position(xpos=.25, xanchor=.25, ypos=.1, yanchor=.1)
        spirit3Spot = Position(xpos=.25, xanchor=.25, ypos=.9, yanchor=.9)
        
        bane1Spot = Position(xpos=.7, xanchor=.7, ypos=.5, yanchor=.5)
        bane2Spot = Position(xpos=.7, xanchor=.7, ypos=.05, yanchor=.05)
        bane3Spot = Position(xpos=.7, xanchor=.7, ypos=.95, yanchor=.95)
        bane4Spot = Position(xpos=.9, xanchor=.9, ypos=.7, yanchor=.7)
        bane5Spot = Position(xpos=.9, xanchor=.9, ypos=.3, yanchor=.3)
        
        bossBane1Spot = Position(xpos=.65, xanchor=.65, ypos=.5, yanchor=.5)
        bossBane2Spot = Position(xpos=.7, xanchor=.7, ypos=.1, yanchor=.1)
        bossBane3Spot = Position(xpos=.7, xanchor=.7, ypos=.9, yanchor=.9)
        
        boss = Position(xpos=1.0, xanchor=.95, ypos=.5, yanchor=.5)

    python:
        class Attack(renpy.Displayable):
            # TODO select an attack to work with the real game
            
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                self.xpos = 200
                self.ypos = 200
                
                self.x = 0
                self.y = 0
                self.turnOver = False
                
                # 0 = normal button
                # 1 = hover over button
                # 2 = clicking button
                self.button = [Image("assets/selectRing/TopLeftCircle.png"), 
                    Image("assets/selectRing/TopLeftCircleHover.png"), 
                    Image("assets/selectRing/TopLeft.png")]
                self.buttonMode = 0
                self.mouseDown = False
            
            # return if cursor is on button
            def isOnButton(self, x, y, angle1, angle2):
                distance = (x - 400)**2 + (y - 400)**2
                if distance >= 10000 and distance <= 40000:
                    angle = math.atan2((y - 400), (x - 400)) * 180 / math.pi
                    return angle > angle1 and angle < angle2
                            
            # rendering cycle
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                pi = renpy.render(self.button[self.buttonMode], 200, 200, st, at)
                
                r.blit(pi, (self.xpos, self.ypos))
                
                text = Text(_("(" + str(self.x) + ", " + str(self.y) + ")"), size=24, color="#ffffff")
                cursor = renpy.render(text, 800, 600, st, at)
                r.blit(cursor, (self.x, self.y))
                
                renpy.redraw(self, 0)
                    
                return r
            
            # Handles events.
            def event(self, ev, x, y, st):
                
                import pygame
                
                # end battle on space, for now 
                # TODO make a real ending thing
                if ev.type == pygame.K_SPACE:
                    self.turnOver = True
                
                # Release mouse, trigger button press
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    self.mouseDown = False
                    if self.isOnButton(x, y, -180, -90):
                        self.turnOver = True
                    
                # Mouse move
                if ev.type == pygame.MOUSEMOTION:
                    self.x = x
                    self.y = y
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
                        return self.turnOver
                    else:
                        raise renpy.IgnoreEvent()
                    
    python:
        # TODO basic functions done, make work with real game
        class Target(renpy.Displayable):
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                self.arrow = Image("assets/x.png")
                
                self.bane1 = True
                self.selected = None
                self.target = False
                
                self.x = 0
                self.y = 0
                
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
                
                text = Text(_("(" + str(self.x) + ", " + str(self.y) + ")"), size=24, color="#ffffff")
                cursor = renpy.render(text, 800, 600, st, at)
                r.blit(cursor, (self.x, self.y))
                
                renpy.redraw(self, 0)
                    
                return r
            
            # Handles events.
            def event(self, ev, x, y, st):
                
                import pygame
                
                # Cancel attack
                if ev.type == pygame.KEYDOWN:
                    print("key pressed")
                    if ev.key == pygame.K_SPACE:
                        print("space pressed")
                        return False
                
                # Mouse move
                if ev.type == pygame.MOUSEMOTION:
                    self.x = x
                    self.y = y
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
                self.xpos = 200
                self.ypos = 200
                self.turnOver = False
                
                self.buttonMode = 0
                self.mouseDown = False


label battle():
    
    window hide None
    scene treeBattle with Dissolve(1)
    
    $ renpy.show("vesto", at_list = [vestoSpot])
    $ renpy.show(pers.img, at_list = [spirit1Spot])
    $ renpy.show(kines.img, at_list = [spirit2Spot])
    $ renpy.show(logi.img, at_list = [spirit3Spot])
    
    #show spirit1 at spirit1Spot
    #show spirit2 at spirit2Spot 
    #show spirit3 at spirit3Spot
    with Dissolve(.5)
    
    $ bossBattle = 1
    if bossBattle:
        show bane1 at bossBane1Spot
        #show bane2 at bossBane2Spot 
        #show bane3 at bossBane3Spot 
        with Dissolve(.5)
        
        show boss at boss with hpunch
    else:
        show bane1 at bane1Spot 
        show bane2 at bane2Spot 
        show bane3 at bane3Spot 
        show bane4 at bane4Spot 
        show bane5 at bane5Spot
        with Dissolve(.5)

    
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
            
            print(target)
            
            if target:
                noTarget = False
        
    return

    $ ui.add(Attack())
    $ ui.interact()
    
    # TODO print who wins and stuff
    return _return
