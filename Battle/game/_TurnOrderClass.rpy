#Receives combatants and manages who goes next
init:
    python:
        
        class TurnOrder(object):
            
            def __init__(self, spirits, banes):
                self.order = []
                self.actors = {}
                for spirit in spirits:
                    self.actors[spirit.ID] = spirit
                for bane in banes:
                    self.actors[bane.ID] = bane
                
                self.sort()
                    
            # return next actor to go, 
            # actors move to 0 using their speed
            def next(self):
                time = self.actors[self.order[0]].timeTillTurn()
                for key, actor in self.actors.items():
                    actor.nextTurnIn -= time
                
                return self.actors[self.order[0]]
            
            # make a temp value to predict actor turn order
            def sort(self):
                self.order = []
                for key, actor in self.actors.items():
                    added = False
                    for i in range(len(self.order)):
                        if actor.timeTillTurn() < self.actors[self.order[i]].timeTillTurn():
                            self.order.insert(i, key)
                            added = True
                            break
                    if not added:
                        self.order.append(key)