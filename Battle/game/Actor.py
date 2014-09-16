import random

class Actor(object):
    
    def __init__(self, name, image, health = 20):
        self.name = name
        self.ID = name
        self.maxHealth = health
        self.damageTaken = 0
        self.img = image
        
    # get spirits current health
    def getHealth(self):
        return (self.maxHealth - self.damageTaken)
        
    # spirit takes damage, cannot go into negative health
    def getHurt(self, amount):
        self.damageTaken += amount
        if self.damageTaken > self.maxHealth:
            self.damageTaken = self.maxHealth
        return self.getHealth()
    
    # spirit gets healed, cannot go above max health
    def getHealed(self, amount):
        self.damageTaken -= amount
        if self.damageTaken < 0:
            self.damageTaken = 0
        return self.getHealth()
            
    # return true if spirit is dead(current health is 0), otherwise false
    def isDead(self):
        return True if self.damageTaken >= self.maxHealth else False
    

# Spirit class
class Spirit(Actor):
    
    def __init__(self, name, image, health = 100, speed = 10, power = 20):
        Actor.__init__(self, name, image, health)
        self.speed = speed
        self.nextTurnIn = 100.0
        self.power = power
        self.statuses = []
        self.bonusPow = 0
        self.dmgMult = 1
        
    # add a status effect, 
    # TODO no duplicates statuses
    def applyStatus(self, status):
        self.statuses.append(status)
        
    # tick statuses and check if any end    
    def checkStatuses(self):
        for status in self.statuses:
            pass
    
    # find attack damage for a given attack power
    def attack(self, atkPow):
        return ((self.power + self.bonusPow) * atkPow) * self.dmgMult

    # returns amount of time until actors turn
    def timeTillTurn(self):
        return self.nextTurnIn / self.speed
    
# Bane Class
class Bane(Actor):
    
    def __init__(self, name, image, health = 100, speed = 10, power = 20):
        Actor.__init__(self, name, image, health)
        self.ID = random.random()
        self.speed = speed
        self.nextTurnIn = 100.0
        self.power = power
        self.statuses = []
        self.bonusPow = 0
        self.dmgMult = 1

    # add a status effect, 
    # TODO no duplicates statuses
    def applyStatus(self, status):
        self.statuses.append(status)
        
    # tick statuses and check if any end    
    def checkStatuses(self):
        for status in self.statuses:
            pass
    
    # find attack damage for a given attack power
    def attack(self, atkPow):
        return ((self.power + self.bonusPow) * atkPow) * self.dmgMult
    
    # returns amount of time until actors turn
    def timeTillTurn(self):
        return self.nextTurnIn / self.speed