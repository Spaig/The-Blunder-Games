class User:
    # team is treated as individual, will include gamemaker - test!

    def __init__(self):
      #self.penalties = 0
      #self.timePenalty = 0   WILL IMPLEMENT LATER :)
      self.currentLandmark = 0
      self.currentUser = ""

    def login(self, username, password):
      pass

    def logout(self, username):
      pass

    def answerQuestion(self, answer):
      # if answer is correct: automatically provide next clue, increments currentLandmark if correct
      pass
    
    def getQuestion(self): #uses currentLandmark in relation to tuple within Game class
      pass

    def getStatus(self): # returns current time, location (penalties accounted for in later iteration)
      pass
    
    def createGame(self): #instantiates new game object and calls setLandmarkList in Game class
      pass
    
    def startGame(self): #only accessible if game maker. This method calls startClock() in Game class
      pass
    
    def endGame(self): #only accessible if game maker
      pass
    
    def createLandmark(self): #gamemaker can create landmark
      pass
    