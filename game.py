import unittest
import landmarks
import time
import system
import user
from gameInterface import gameInterface

# Testing
class Game(gameInterface):
    def __init__(self, currentsystem):
        ##THE ~FUTURE~ self.clock = 0  # need to import time or some other 3rd party clock
        self.isActive = False  # game is active when gamemaker calls startGame (and startClock)
        self.landmarkList = []  # ordered list of landmarks
        self.System = currentsystem  # needs to have system passed in from controller so to have access to landmarks/teams in DB
        self.teams = []  # list of user objects in game to retain stateful data of each team


    # holds game landmarks, anything stored within the game
    def addTeamToGame(self, teamName, password):
        usr = user.User(teamName, password)
        self.teams.append(usr)


    def checkIfWin(self, x):
        return x == (len(self.landmarkList))

    ##THE ~FUTURE~ def getClock(self):
        ##THE ~FUTURE~ return self.clock

    def getLandmarkList(self):
        return self.landmarkList

    def getTeams(self):
        return self.teams


    # Sets landmarkList to a given list of landmarks passed in. Must be game maker.
    def setLandmarkList(self, landmarks):
        if landmarks != None:
          self.landmarkList = landmarks

    ##THE ~FUTURE~ def startClock(self):
    ##THE ~FUTURE~     pass

    ##THE ~FUTURE~ def stopClock(self):
     ##THE ~FUTURE~    pass 

    def toggleActive(self):
        if (self.isActive):
         ##THE ~FUTURE~  self.stopClock()
          self.isActive = False
        else:
        ##THE ~FUTURE~   self.startClock()
          self.isActive = True




class TestAddTeamsToGame(unittest.TestCase):  # Thomas
    def setUp(self):
        self.User = user.User()
        self.System = system.System()
        self.Game = Game(self.System)
        self.System.teams = {"username": "password", "TeamB": "otherpass", "TeamC": "Lincoln"}

    def test_AddUser(self):
        self.Game.addTeamToGame("TeamB")
        self.assertEquals(self.Game.teams[0], "TeamB", "TeamB should be first in currentTeams")
        self.Game.addTeamToGame("TeamC")
        self.assertEquals(len(self.Game.teams), 2, "Should have two teams in the game")

    def test_NotGameMaker(self):
        self.User.currentUser = "username"
        self.assertEquals(self.Game.addTeamToGame("TeamB"), "ERROR", "Game maker must be current user to add to game.")


class TestGetLandmarkList(unittest.TestCase):
    def setUp(self):
        self.System = system.System()
        self.Game = Game(self.System)
        self.Game.landmarkList = ["Road", "Park"]

    def test_normalGetLandmark(self):
        self.assertEqual(self.Game.getLandmarkList(), ["Road", "Park"], "Return of getLandmarkList() not accurate")
        self.Game.landmarkList = ["Apartment", "The Alamo"]
        self.assertEqual(self.Game.getLandmarkList(), ["Apartment", "The Alamo"], "LandmarkList incorrect after change")

    def test_emptyGetLandmark(self):
        self.Game.landmarkList = []
        self.assertEqual(self.Game.getLandmarkList(), [],
                         "Call to getLandmarkList() when list is empty should return an empty list")


class TestToggleActive(unittest.TestCase):
    def setUp(self):
        self.System = system.System()
        self.Game = Game(self.System)

    def test_normalToggle(self):
        self.assertFalse(self.Game.isActive, "Game starting out active")
        self.Game.toggleActive()
        self.assertTrue(self.Game.isActive, "Game is not active after call to toggleActive()")
        
