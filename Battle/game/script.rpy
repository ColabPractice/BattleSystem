# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    
    image office = "assets/office.png"
    
    python:
        #config.keymap['dismiss'].remove('K_SPACE')
        #config.keymap['hide_windows'].append('K_SPACE')
        pass
    
    python:
        
        # TODO start spirit and bane class
        class Spirit():
            
            def __init__(self, fName = "spirit", lName = "thing"):
                self.displayName = fName
                self.firstName = fName
                self.lastName = lName
                self.speed = int(10)
                self.maxHealth = 100
                self.power = 20
                self.img = "pers normal"
            
        
    $ aaa = Spirit(fName = "pers")

# Declare characters used by this game.
define e = Character('Eileuppipiuoen', color="#c8ffc8")


# The game starts here.
label start:
    
    scene office

    "Start game"
    
    call battle()
    scene office with Dissolve(1)
    
    $ renpy.say("", _return)
    "Game end"