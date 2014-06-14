# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    
    image office = "assets/office.png"
    image pers = "assets/cPers.png"
    
    python:
        #config.keymap['dismiss'].remove('K_SPACE')
        #config.keymap['hide_windows'].append('K_SPACE')
        pass
    
    python:
        
        # TODO start spirit and bane class
        #Spirit Class
        class Spirit():
            
            def __init__(self, name, image, health = 100, speed = 10, power = 20):
                self.name = name
                self.maxHealth = health
                self.speed = speed
                self.power = power
                self.damageTaken = 0
                self.img = image
                
            def getHealth(self):
                return (self.maxHealth - self.damageTaken)
                
            def getHurt(self, amount):
                self.damageTaken += amount
                if self.damageTaken > self.maxHealth:
                    self.damageTaken = self.maxHealth
                
            def getHealed(self, amount):
                self.damageTaken -= amount
                if self.damageTaken < 0:
                    self.damageTaken = 0
                    
            def isDead(self):
                return True if self.damageTaken >= self.maxHealth else False
        
        #Bane Class
        class Bane():
            
            def __init__(self, name, imageLocation, health = 100, speed = 10, power = 20):
                self.name = name
                self.maxHealth = health
                self.speed = speed
                self.power = power
                self.damageTaken = 0
                self.img = imageLocation
                
            def getHealth(self):
                return (self.maxHealth - self.damageTaken)
                
            def getHurt(self, amount):
                self.damageTaken += amount
                if self.damageTaken > self.maxHealth:
                    self.damageTaken = self.maxHealth
                
            def getHealed(self, amount):
                self.damageTaken -= amount
                if self.damageTaken < 0:
                    self.damageTaken = 0
                    
            def isDead(self):
                return True if self.damageTaken >= self.maxHealth else False
                
        
        # TODO Make the system do Shit, Maybe.
                
    $ cPers = Spirit("Pers", "pers")

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