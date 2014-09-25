# Initilization info in _init.rpy file

# The game starts here.
label start:
    
    scene office
    
    show pers battle
    "show per battle"

    $ spirits[0] = pers
    $ spirits[1] = logi
    $ spirits[2] = kines
    
    $ banes[0] = bob
    $ banes[1] = bane
    
    scene
    call battle()
    scene office
    
    $ renpy.say("", _return)
    "Game end"