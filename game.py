class Game:
    def __init__(self):
        self.clock = 0        #need to import time or some other 3rd party clock        
        self.isActive = False  #game is active when gamemaker calls startGame (and startClock)
        self.landmarkList = ()   #specific order of landmarks

    # holds game landmarks, anything stored within the game
    
    def setLandmarkList(self, x):
      pass
    
    def startClock(self):
      pass
    
    def stopClock(self):
      pass