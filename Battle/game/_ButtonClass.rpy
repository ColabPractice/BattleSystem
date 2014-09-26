# Button class to be used in the battle
init:
    python:
        
        class Button(object):
            
            def __init__(self, x, y, text = "", icon = None):
                # 0 = normal button
                # 1 = hover over button
                # 2 = clicking button

                self.image = [Image("assets/button.png"),
                    Image("assets/button_hover.png"),
                    Image("assets/button_click.png")]
                
                self.icon = icon
                self.text = text
                self.posX = x
                self.posY = y
                self.buttonMode = 0
                self.visible = True
            
            # return if coords are within 37.5 of the button and button is visible
            def isOnButton(self, x, y):
                distance = (x - self.posX - 75/2)**2 + (y - self.posY - 75/2)**2
                if distance <= (75/2)**2:
                    return self.visible
                
            def getImage(self):
                return self.image[self.buttonMode]
            