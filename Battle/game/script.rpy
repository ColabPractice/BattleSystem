# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:

    image office = "assets/office.png"
    image pers = im.Scale("assets/cPers.png", 180, 200)
    image logi = "mario-icon.png"
    image kines = im.Flip(im.Scale("assets/weakhearth.png", 150, 150), horizontal = True, vertical = True)
    
    
    python:
        #config.keymap['dismiss'].remove('K_SPACE')
        #config.keymap['hide_windows'].append('K_SPACE')
        pass

        # TODO spirit and bane class stuff?
        # TODO Make the system do Shit, Maybe.
                
    

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    
    scene office

    "Start game"
    #$ renpy.show(cPers.img) #THIS WORKS OMFG
    
    call battle()
    scene office with Dissolve(1)
    
    $ renpy.say("", _return)
    "Game end"