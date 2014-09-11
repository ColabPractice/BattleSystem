# Initilization info in _init.rpy file

# The game starts here.
label start:
    
    scene office
    
    show per battle
    "show per battle"
    
    show per battlesmall mad
    "show per battlesmall mad"
    
    call battle()
    scene office with Dissolve(1)
    
    $ renpy.say("", _return)
    "Game end"