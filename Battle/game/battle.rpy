init:
    image bg = "assets/trees.jpg"
    
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

screen attack():
    # TODO make it select an attack and a target after attack selected
    key "K_SPACE" action Return("aaa")

label battle():
    
    window hide None
    scene bg with Dissolve(1)
    
    $ renpy.show("vesto", at_list = [vestoSpot])
    show spirit1 at spirit1Spot with Dissolve(.5)
    show spirit2 at spirit2Spot with Dissolve(.5)
    show spirit3 at spirit3Spot with Dissolve(.5)
    $ bossBattle = 0
    if bossBattle:
        show bane1 at bossBane1Spot with Dissolve(.5)
        show bane2 at bossBane2Spot with Dissolve(.5)
        show bane3 at bossBane3Spot with Dissolve(.5)
        show boss at boss with Dissolve(.5)
    else:
        show bane1 at bane1Spot with Dissolve(.5)
        show bane2 at bane2Spot with Dissolve(.5)
        show bane3 at bane3Spot with Dissolve(.5)
        show bane4 at bane4Spot with Dissolve(.5)
        show bane5 at bane5Spot with Dissolve(.5)
    
    
#    python:
#        def clicky():
#            renpy.sound.play('assets/smw_1-up.wav')
        
#        ui.imagebutton(Image('Mario-icon.png')
#            , im.MatrixColor(Image('Mario-icon.png'), im.matrix.invert())
#            , Image('Mario-icon.png')
#            , clicked = clicky)
    
    call screen attack()
    
    # TODO print who wins and stuff
    return _return