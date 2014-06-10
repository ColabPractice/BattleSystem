init:
    image bg = "assets/trees.jpg"
    
    python:
        
        config.keymap['dismiss'].remove('K_SPACE')
        config.keymap['hide_windows'].append('K_SPACE')
        # config.keymap['quit'].append('K_SPACE')
        
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
    
    
    
init python:
        
    class battlefield(renpy.Displayable):
        
        def __init__(self):
            
            renpy.Displayable.__init__(self)
            
            self.xpos = 0
            self.ypos = 0
            self.battleOver = None
            
            # The time of the past render-frame.
            self.oldst = None
        
        # TODO decide if render function is needed, likely yes because of buttons
        # and other possible small animations on the UI
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st
            
            pi = renpy.render(Image("Mario-icon.png"), 256, 256, st, at)
            
            r.blit(pi, (self.xpos, self.ypos))
            
            renpy.redraw(self, 0)
                
            return r
            
        # Handles events.
        def event(self, ev, x, y, st):

            import pygame
           
            # end battle on click, for now 
            # TODO make a real ending thing
            if ev.type == pygame.MOUSEBUTTONUP:
                self.battleOver = "yes"
                #renpy.timeout(0)
            
            # Move mario around and shit
            self.xpos = x - 128
            self.ypos = y - 128

            # Some kind of battle ending mechanic?
            if self.battleOver:
                return self.battleOver
            else:
                raise renpy.IgnoreEvent()
            
label battle:
    
    scene bg
    #$ renpy.say(aaa.displayName, spirit1Spot)
    #hide dialogue window
    window hide None
    
    $ renpy.show("vesto", at_list = [vestoSpot])
    

    #show vesto at vestoSpot
    show spirit1 at spirit1Spot
    show spirit2 at spirit2Spot
    show spirit3 at spirit3Spot
    $ bossBattle = 1
    if bossBattle:
        show bane1 at bossBane1Spot
        show bane2 at bossBane2Spot
        show bane3 at bossBane3Spot
        #show bane4 at bossBane4Spot
        #show bane5 at bossBane5Spot
        show boss at boss
    else:
        show bane1 at bane1Spot
        show bane2 at bane2Spot
        show bane3 at bane3Spot
        show bane4 at bane4Spot
        show bane5 at bane5Spot

    
    $ ui.add(battlefield())
    $ ui.interact()
    
    #show dialogue window?
    window show None

    # TODO print who wins and stuff
    
    return "battle return"