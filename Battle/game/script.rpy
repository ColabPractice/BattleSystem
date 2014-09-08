# Initilization info in _init.rpy file

import _init

# The game starts here.
label start:
    
    scene office
    
    $ print(pers.img)
    $ renpy.show(pers.img) #THIS WORKS OMFG
    
    "show pers"
    
    call battle()
    scene office with Dissolve(1)
    
    #$ renpy.say("", _return)
    "Game end"