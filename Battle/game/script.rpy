# Initilization info in _init.rpy file

# The game starts here.
label start:
    
    scene office
    
    $ renpy.show(pers.img)
    
    "show pers"
    
    call battle()
    scene office with Dissolve(1)
    
    #$ renpy.say("", _return)
    "Game end"