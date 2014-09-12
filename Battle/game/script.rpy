# Initilization info in _init.rpy file

# The game starts here.
label start:
    
    scene office
    
    show pers battle
    "show per battle"

    $ party1 = pers
    $ party2 = logi
    $ party3 = kines
    
    scene
    call battle()
    scene office with Dissolve(1)
    
    $ renpy.say("", _return)
    "Game end"