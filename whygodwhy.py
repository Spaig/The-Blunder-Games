import abc

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
    
      
class Landmarks:
    def __init__(self, name, clue, question, answer):
      self.name = name
      self.clue = clue
      self.question = question
      self.answer = answer
      
    def setClue(self, clue): #to be called by gamemaker
      self.clue = clue
      
    def setQuestion(self, question): #to be called by gamemaker
      self.question = question
      
    def setAnswer(self, answer): #to be called by gamemaker
      self.answer = answer

class Interface:
    def __init__(self):
        pass
    def command(self, commandString):
        pass

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

class System:

    # pseudo database, way to interact with lists
    def __init__(self):
        self.landmarks = []  # [landmark objects]
        self.teams = {"admin": "kittens", }  # gamemaker hardcoded in


