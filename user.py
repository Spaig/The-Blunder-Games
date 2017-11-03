import unittest
import landmarks


class User:
    # team is treated as individual, will include gamemaker - test!

    def __init__(self):
        # self.penalties = 0
        # self.timePenalty = 0   WILL IMPLEMENT LATER :)
        self.name = ""
        self.gm = False
        self.system = system.System()

    '''
    def login(self, username, password):
        if self.system.teams[username] != password:
            print("Username or password is incorrect")
            self.name = ""
        else:
            self.name = username

    def logout(self, username):
        pass  # TODO
    '''

    def answer_question(self, answer):
        # if answer is correct: automatically provide next clue, increments controller.currentLandmark if correct
        pass  # TODO

    def get_question(self):
        # uses controller.currentLandmark in relation to tuple within Game class
        pass  # TODO

    def get_status(self):
        # returns current time, location (penalties accounted for in later iteration)
        pass  # TODO

    def create_game(self, landmark, teams):
        # instantiates new game object and calls setLandmarkList & setTeams in Game class. Current user is admin
        pass  # TODO

    def start_game(self):
        # only accessible if game maker. This method calls startClock() in Game class
        pass  # TODO

    def end_game(self):
        # only accessible if game maker
        pass  # TODO

    def create_landmark(self, name, clue, question, answer):
        # gamemaker can create landmark
        pass  # TODO


class TestAcceptanceQuestions(unittest.TestCase):
    def setUp(self):
        self.system = system.System()
        self.user = self.user()
        self.controller = controller.Controller()
        river = self.system.landmarks("River", "test1", "test2", "test3")
        tree = self.system.landmarks("Tree", "blah1", "blah2", "blah3")
        place = self.system.landmarks("Place", "asdf1", "asdf2", "asdf3")
        self.system.landmarks = [tree, river]

    def test_answer_question_correct(self):
        self.controller.currentLandmark = 0
        self.assertEquals(self.user.answer_questionn("test3"), "Correct!", "Should be the correct answer.")

    def test_answer_question_wrong(self):
        self.controller.currentLandmark = 0
        self.assertEquals(self.user.answer_questionn("Cats r kewl"), "Wrong, try again", "Incorrect answer entered")


class TestAcceptanceUserStatus(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.controller = controller.Controller()
        self.user = self.user()
    def test_userStatusCurrent(self):
        self.game.isActive = True
        self.game.clock = 5
        self.controller.currentLandmark = 1
        self.assertEquals(self.user.get_status(), "Time: 5, Landmark: 2", "User cannot access current status during game")


class TestAcceptanceGMStatus(unittest.TestCase):  # TODO
    def setup(self):
        self.game = game.Game()

    def test_gm_status_current(self):
        pass


class TestGame(unittest.TestCase):
    def setUp(self):
        self.Game = game.Game()

    def test_game_start(self):
        pass

    def test_game_end_gm(self):
        pass

    def test_gameEndUser(self):
        self.Game.isActive = True
        self.controller.currentLandmark = 4
        self.assertFalse(self.Game.isActive, "Game is not over")


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
Acceptance not needed
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


class TestGMAddLandmark(unittest.TestCase):  # Chris Kirst
    def setUp(self):
        self.System = system.System()
        self.User = User()
        self.User.currentUser = "admin"
        self.Landmark = None
        self.System.teams = {"admin": "kittens"}

    def testAddLandMark(self):
        self.User.createLandmark("park", "there are benches", "who is fountain dedicated to?", "St. Python")
        self.Landmark = self.System.landmarks[0]
        self.assertEquals(self.Landmark.name, "park", "Landmark name is not correct")
        self.assertEquals(self.Landmark.clue, "there are benches", "Landmark question is not correct")
        self.assertEquals(self.Landmark.question, "who is the fountain dedicated to?",
                          "Landmark question is not correct")
        self.assertEquals(self.Landmark.answer, "St. Python", "Landmark answer is not correct")
        self.assertIn(self.Landmark, self.System.landmarks, "Landmark just created should be in system")
        self.Landmark = landmarks.Landmark("Lab", "The room is on the 9th floor", "How many Macs are in the room?",
                                           "20")
        self.assertNotIn(self.Landmark, self.System.landmarks, "Landmark should not be in the system")

    def testAddExistingLandmark(self):
        self.User.createLandmark("place", "clue", "question", "answer")
        self.assertEquals(
            self.User.createLandmark("place", "clue", "question", "answer", "Landmark already exists in System",
                                     "Cannot add duplicate landmarks to system!"))

    def testAddBadLandmark(self):
        self.assertEquals(self.User.createLandmark("", "", "", ""), "Invalid landmark argument(s)",
                      "Adding blank landmark should fail")


class TestGMCreateNewGame(unittest.TestCase):  # Chris Kirst
    def setUp(self):
        self.User()
        self.System()
        self.Game = None
        self.System.teams = {"admin": "pass123", "teamA": "passwordA", "teamB": "passwordB"}
        x = landmarks.Landmark("park", "", "", "")
        y = landmarks.Landmark("lab", "", "", "")
        z = landmarks.Landmark("library", "", "", "")
        self.System.landmarks = [x, y, z]

    def CreateGame(self):
        self.Game = self.User.createGame("park,lab,library", "teamA,teamB")
        self.assertEquals(self.Game.controller.currentLandmarks[0].name, "park", "First landmark not correct")
        self.assertEquals(self.Game.controller.currentLandmarks[1].name, "lab", "Second landmark not correct")
        self.assertEquals(self.Game.controller.currentLandmarks[2].name, "library", "Third landmark not correct")
        self.assertNotIn("union", self.Game.controller.currentLandmarks, "union should not be in current landmark list")
        self.assertIn("teamA", self.Game.currentTeams, "teamA should be in game")
        self.assertIn("teamB", self.Game.currentTeams, "teamB should be in game")
        self.assertNotIn("teamC", self.Game.currentTeams, "teamC should NOT be in game")
        self.assertEqual(self.Game.clock, 0, "Clock should not be started until Game maker initiates game")
        self.assertFalse(self.Game.isActive, "Game should not be active until started.")
