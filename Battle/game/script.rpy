# Initilization info in _init.rpy file

# The game starts here.
label start:
    
    scene office
    
    show pers battle
    "show per battle"

    $ party[0] = pers
    $ party[1] = logi
    $ party[2] = kines
    
    scene
    call battle(bossBattle = True)
    scene office with Dissolve(1)
    
    $ renpy.say("", _return)
    "Game end"