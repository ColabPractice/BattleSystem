#Receives combatants and manages who goes next
import Actor
class turnOrder(object):
    
    def __init__(self, spirits, banes):
        #self.order = []
        self.people = {}
        for spirit in spirits:
            self.people[spirit.ID] = spirit
            #self.order.append(spirit.ID)
        for bane in banes:
            self.people[bane.ID] = bane
            #self.order.append(bane.ID)
        
#        while True:
#            swapped = False
#            for i in range(len(self.order) - 1):
#                if self.people[self.order[i]].speed < self.people[self.order[i + 1]].speed:
#                    swapped = True
#                    temp = self.order[i]
#                    self.order[i] = self.order[i + 1]
#                    self.order[i + 1] = temp
#            if not swapped:
#                break
            
    # return next actor to go, 
    # actors move to 1000 using their speed
    # at 1000 or past, 
    def next():
        while True:
            pass
    
    # make a temp value to predict actor turn order
    def order():
        pass