init:
    image bg = "assets/trees.jpg"
    
    $ import Actor
    $ import math

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
            # TODO make it select an attack and a target after attack selected
            
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                self.xpos = 200
                self.ypos = 200
                self.battleOver = None
                
                self.hover = False
                self.button = Image("assets/selectRing/TopLeftCircle.png")
                self.buttonHover = Image("assets/selectRing/TopLeftCircleHover.png")
                
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                pi = renpy.render(self.buttonHover if self.hover else self.button, 200, 200, st, at)
                
                r.blit(pi, (self.xpos, self.ypos))
                
                renpy.redraw(self, 0)
                    
                return r
            
            # TODO button clicking stuff
            # Handles events.
            def event(self, ev, x, y, st):
                
                import pygame
                
                # end battle on click, for now 
                # TODO make a real ending thing
                if ev.type == pygame.K_SPACE:
                    self.battleOver = "yes"
                    renpy.timeout(0)
                
                # Move mario around and shit
                distance = (x - 400)**2 + (y - 400)**2
                if distance >= 10000 and distance <= 40000:
                    angle = math.atan2((y - 400), (x - 400)) * 180 / math.pi
                    if angle > -180 and angle < -90:
                        self.hover = True
                    else:
                        self.hover = False
                else:
                    self.hover = False
                #self.xpos = x - 128
                #self.ypos = y - 128

                # Some kind of battle ending mechanic?
                if self.battleOver:
                    return self.battleOver
                else:
                    raise renpy.IgnoreEvent()

label battle():
    
    window hide None
    scene bg with Dissolve(1)
    
    $ renpy.show("vesto", at_list = [vestoSpot])
    $ renpy.show(cPers.img, at_list = [spirit1Spot])
    $ renpy.show(cKines.img, at_list = [spirit2Spot])
    $ renpy.show(cLogi.img, at_list = [spirit3Spot])
    
    #show spirit1 at spirit1Spot
    #show spirit2 at spirit2Spot 
    #show spirit3 at spirit3Spot
    with Dissolve(.5)
    
    $ bossBattle = 1
    if bossBattle:
        show bane1 at bossBane1Spot
        show bane2 at bossBane2Spot 
        show bane3 at bossBane3Spot 
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
    
    $ ui.add(Attack())
    $ ui.interact()
    
    # TODO print who wins and stuff
    return _return