# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    
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
                self.img = "Mario-icon.png"
            
        
    $ aaa = Spirit(fName = "pers")

# Declare characters used by this game.
define e = Character('Eileuppipiuoen', color="#c8ffc8")


# The game starts here.
label start:
    
    scene office

    "start game"
    # $ name = aaa.firstName
    $ name = "unchanged name"
    "[name!t]"
    call battle
    $ name = _return
    
    scene office
    
    "[name!t]"