import random

# Spirit class
class Spirit(object):
    
    def __init__(self, name, image, health = 100, speed = 10, power = 20):
        self.name = name
        self.ID = name
        self.maxHealth = health
        self.speed = speed
        # TODO make 'getting ready' method, progress towards actors turn
        self.nextTurn = speed
        self.power = power
        self.damageTaken = 0
        self.img = image
        self.statuses = []
        self.bonusPow = 0
        self.dmgMult = 1
        
    # get spirits current health
    def getHealth(self):
        return (self.maxHealth - self.damageTaken)
        
    # spirit takes damage, cannot go into negative health
    def getHurt(self, amount):
        self.damageTaken += amount
        if self.damageTaken > self.maxHealth:
            self.damageTaken = self.maxHealth
    
    # spirit gets healed, cannot go above max health
    def getHealed(self, amount):
        self.damageTaken -= amount
        if self.damageTaken < 0:
            self.damageTaken = 0
            
    # return true if spirit is dead(current health is 0), otherwise false
    def isDead(self):
        return True if self.damageTaken >= self.maxHealth else False
    
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

# Bane Class
class Bane(object):
    
    def __init__(self, name, imageLocation, health = 100, speed = 10, power = 20):
        self.name = name
        self.ID = random.random()
        self.maxHealth = health
        self.speed = speed
        self.power = power
        self.damageTaken = 0
        self.img = imageLocation
        self.statuses = []
        self.bonusPow = 0
        self.dmgMult = 1
    
    # get bane current health
    def getHealth(self):
        return (self.maxHealth - self.damageTaken)
    
    # bane takes damage, cannot go into negative health
    def getHurt(self, amount):
        self.damageTaken += amount
        if self.damageTaken > self.maxHealth:
            self.damageTaken = self.maxHealth
    
    # bane gets healed, cannot go above max health
    def getHealed(self, amount):
        self.damageTaken -= amount
        if self.damageTaken < 0:
            self.damageTaken = 0
    
    # return true if bane is dead(current health is 0), otherwise false
    def isDead(self):
        return True if self.damageTaken >= self.maxHealth else False
        
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