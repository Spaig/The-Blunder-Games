import unittest, time, system, user

class Game:
    def __init__(self):
        self.clock = 0        #need to import time or some other 3rd party clock        
        self.isActive = False  #game is active when gamemaker calls startGame (and startClock)
        self.landmarkList = ()   #specific order of landmarks
        self.currentTeams = [] #list of teams in the current game
        
    # holds game landmarks, anything stored within the game
    
    def setLandmarkList(self, landmarks):
      pass
    
    def setTeams(self, teams): #add existing team to current game?
      pass
    
    def startClock(self):
      pass
    
    def stopClock(self):
      pass
    
class TestAddTeamstoGame(unittest.TestCase): #Thomas
  def setUp(self):
    self.User = user.User()
    self.Game = Game()
    self.System = system.System()
    self.System.teams = {"username":"password","TeamB":"otherpass","TeamC":"Lincoln"}
  def testAddUser(self):
    self.Game.setTeams("TeamB")
    self.assertEquals(self.Game.currentTeams[0], "TeamB", "TeamB should be first in currentTeams")
    self.Game.setTeams("TeamC")
    self.assertEquals(len(self.Game.currentTeams), 2, "Should have two teams in the game")
  def testNotGameMaker(self):
    self.User.currentUser = "username"
    self.assertEquals(self.Game.setTeams("TeamB"), "ERROR", "Game maker must be current user to add to game.")
    
    