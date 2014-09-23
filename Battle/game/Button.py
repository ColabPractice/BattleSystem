# Button class to be used in the battle

class CircleButton(object):
    
    __init__(self, image):
        # 0 = normal button
        # 1 = hover over button
        # 2 = clicking button
        # 3 = disabled
        self.image = image
        
        self.text = ""
        self.posX = 0
        self.posY = 0
        self.angle1 = angle1
        self.angle2 = angle2
        self.buttonMode = 0
    
    def isOnButton(self, x, y):
        distance = (x - 400)**2 + (y - 400)**2
        if distance >= 10000 and distance <= 40000:
            angle = math.atan2((y - 400), (x - 400)) * 180 / math.pi
            return angle > self.angle1 and angle < self.angle2
        return False