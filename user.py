import unittest
from userInterface import userInterface
import landmarks
import system
import game

#Changing User implementation Sprint 2. Will only contain Name, pass, and currentLandmark. 

class User(userInterface):
    # team is treated as individual, will include gamemaker - test!

    def __init__(self, username, password):
        # self.penalties = 0
        # self.timePenalty = 0   WILL IMPLEMENT LATER :)
        self.name = username
        self.password = password
        self.System = system.System
        self.currentLandmark = 0  # indicates position in game's landmarkList
       # self.Game = game.Game(self.System)

    def getName(self):
      return self.name
    
    def getPassword(self):
      return self.password

    

    def get_status(self):
       # returns current time, location (penalties accounted for in later iteration)
      #if gm
      #implement gm total status sprint 2
        print("Stats for %s", self.name)
        #print("Current time: %d", self.Game.clock)  # TODO: need to fix this line
        print("You are on landmark %d !", self.currentLandmark)  # Prints name of landmark



class TestAcceptanceQuestions(unittest.TestCase):
    def setUp(self):
        self.system = system.System()
        self.user = self.user()
        # self.controller = controller.Controller()
        river = self.system.landmarks("River", "test1", "test2", "test3")
        tree = self.system.landmarks("Tree", "blah1", "blah2", "blah3")
        place = self.system.landmarks("Place", "asdf1", "asdf2", "asdf3")
        self.system.landmarks = [tree, river]

    def test_answer_question_correct(self):
        self.user.currentLandmark = 0
        self.assertEquals(self.user.answer_question("test3"), "Correct!", "Should be the correct answer.")

    def test_answer_question_wrong(self):
        self.user.currentLandmark = 0
        self.assertEquals(self.user.answer_question("Cats r kewl"), "Wrong, try again", "Incorrect answer entered")


class TestAcceptanceUserStatus(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        # self.controller = controller.Controller()
        self.user = self.user()

    def test_userStatusCurrent(self):
        self.game.isActive = True
        self.game.clock = 5
        self.user.currentLandmark = 1
        self.assertEquals(self.user.get_status(), "Time: 5, Landmark: 2", "User cannot access current status during game")


class TestAcceptanceGMStatus(unittest.TestCase):  # TODO
    def setup(self):
        self.game = game.Game()

    def test_gm_status_current(self):
        pass


# Is this class needed here? -Derek
class TestGame(unittest.TestCase):
    def setUp(self):
        self.Game = game.Game()
        self.user = User("admin", "kittens")

    def test_game_start(self):
        pass

    def test_game_end_gm(self):
        pass

    def test_gameEndUser(self):
        self.Game.isActive = True
        self.user.currentLandmark = 4
        self.assertFalse(self.Game.isActive, "Game is not over")


'''
class TestLogin(unittest.TestCase):  # derek's tests
    def setUp(self):
        self.User = User()
        self.System = system.System()
        self.System.teams = {"username": "password", "Gerard": "otherpass", "Humphrey": "Lincoln"}

    def test_NormalLogin(self):
        self.User.login("username", "password")
        self.assertEquals(self.User.name, "username", "Current user is not username")
        self.User.login("Gerard", "otherpass")
        self.assertEquals(self.User.name, "Gerard", "Current user is not Gerard");
        self.User.login("Humphrey", "Lincoln")
        self.assertEquals(self.User.name, "Humphrey", "Current user is not Humphrey")

    def test_BadPassword(self):
        self.User.login("username", "badpass")
        self.assertEquals(self.User.name, "", "Current user should still be empty on a wrong password")

    def test_BadUsername(self):
        self.User.login("Gerry", "otherpass")
        self.assertEquals(self.User.name, "", "Current user should still be empty on a wrong username")

    def test_BadUsernameAndPass(self):
        self.User.login("Hrey", "Locolon")
        self.assertEquals(self.User.name, "", "Current user should still be empty on a wrong username and password")

    def test_EmptyLogin(self):
        self.User.login("", "")
        self.assertEquals(self.User.name, "", "Current user should still be empty on nothing entered")
'''

'''
class TestLoginAcceptance(unittest.TestCase):
  def setUp(self):
    self.Interface = Interface()
    self.User = User()
    self.System = System()
    self.System.teams = {"username":"password","Gerard":"otherpass","Humphrey":"Lincoln"}
  def test_NormalLogin(self):
    self.Interface.command("login(\"username\",\"password\")")
    self.assertEquals(self.User.currentUser, "username", "Current user is not username")
    self.Interface.command("login(\"Gerard\",\"otherpass\")")
    self.assertEquals(self.User.currentUser, "Gerard", "Current user is not Gerard");
    self.Interface.command("login(\"Humphrey\",\"Lincoln\""))
    self.assertEquals(self.User.currentUser, "Humphrey", "Current user is not Humphrey")
  def testBadPassword(self):
    self.Interface.command("login(\"username\",\"badpass\")")
    self.assertEquals(self.User.currentUser, "", "Current user should still be empty on a wrong password")
  def testBadUsername(self):
    self.Interface.command("login(\"Gerry\",\"otherpass\")")
    self.assertEquals(self.User.currentUser, "", "Current user should still be empty on a wrong username")
  def testBadUsernameAndPass(self):
    self.Interface.command("login(\"Idontexist\",\"help\")")
    self.assertEquals(self.User.currentUser, "", "Current user should still be empty on a wrong username and password")
  def testEmptyLogin(self):
    self.Interface.command("login(\"\",\"\")")
    self.assertEquals(self.User.currentUser, "", "Current user should still be empty on nothing entered")

'''