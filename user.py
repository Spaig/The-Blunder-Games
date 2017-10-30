import unittest, game, time

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
    
class TestQuestion(unittest.TestCase):
  def setUp(self):
    self.default = game.game()
    
  def test_getQuestion1(self):
    pass
  
  def test_getQuestion2(self):
    pass
  
  def test_getQuestion3(self):
    pass
  
  def test_answerQuestion1(self):
    pass
  
  def test_answerQuestion2(self):
    pass
  
  def test_answerQuestion3(self):
    pass
  
  def test_getClue1(self):
    self.assertEqual(self.currentLandmark, 1, "currentLandmark not 0")
  
  def test_getClue2(self):
    self.assertEqual(self.currentLandmark, 1, "currentLandmark not 1")
  
  def test_getClue3(self):
    self.assertEqual(self.currentLandmark, 1, "currentLandmark not 2")
    
class TestUserStatus(unittest.TestCase):
  def setUp(self):
    self.default = self.game.game()
  def test_userStatusCurrentLocation(self):
    self.default.isActive = True
    self.assertEqual(self.game.landmarkList(0), self.game.landmarkList(currentLandmark), "current landmark status mismatch during game")
  def test_userStatusCurrentTime(self):
    self.default.isActive = True
    self.tick = self.time.clock()
    self.time.sleep(0.1)
    self.assertEqual(self.default.clock, self.tick, "current time status mismatch during game")
  def test_userStatusEnd(self):
    pass
  def test_gamemakerStatusCurrent(self):
    pass
  def test_gamemakerStatusEnd(self):
    pass

class TestAcceptanceUserStatus(unittest.TestCase):
  def setUp(self):
    self.default = self.game.game()
  def test_userStatusCurrent(self):
    self.default.isActive = True
    self.tick = self.time.clock()
    assertEquals(self.getStatus(), "", "User cannot access current status during game") #TODO getStatus message
    
class TestGame(unittest.TestCase):
  def setUp(self):
    self.default = self.game.game()
  def test_gameStart(self):
    pass
  def test_gameEndGamemaker(self):
    pass
  def test_gameEndUser(self):
    self.default.isActive = True
    self.currentLandmark = 4
    self.assertFalse(self.default.isActive, "Game is not over")
    