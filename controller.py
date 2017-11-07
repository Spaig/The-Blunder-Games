import unittest
import system
import user
import game


class Controller:
    def __init__(self):
        self.currentUser = None
        self.Game = None
        self.System = system.System()

    def check(self, parsedText, currentUser):  # where parsedText is a list of strings
        # if user=None, don't accept any method except login
        # elif tree of different methods depending on first index of parsedText
        # a = eval('A')
        command = parsedText[0]
        if command == 'login' or 'Login':
            pass
        elif command == 'logout' or 'Logout':
            pass
        elif command == 'start' or 'Start':
            pass
        elif command == 'create' or 'Create':
            pass
        elif command == 'end' or 'End':
            pass

    # def getInstance(self):
    # Game maker must be first to log in?
    def login(self, username, password):
        if self.System.getTeamPassword(username) == password:
            self.currentUser = username
            print("Successfully logged in")
        else:
            print("Username or password is incorrect")

    def logout(self):
        self.currentUser = None
        print("User logged out")

    def create_game(self, landmark, teams):
        # instantiates new game object and calls setLandmarkList & setTeams in Game class. Current user is admin
        if self.currentUser != "admin":
            print("Cannot create game if not game maker")
        else:
            pass

    def start_game(self):
        # only accessible if game maker. This method calls startClock() in Game class
        if (self.currentUser == "admin"):
            if self.Game.isActive:
              print("There is already an active game")
            else:
              self.Game.toggleActive()
        else:
            print("Cannot start game if not game maker")

    def end_game(self):
        # only accessible if game maker
        if (self.currentUser == "admin"):
            if not self.Game.isActive:
              print("There is no active game")
            else:
              self.Game.toggleActive()
            # more?
        else:
            print("Cannot end game if not game maker")
        pass  # TODO

    def create_landmark(self, name, clue, question, answer):
        # gamemaker can create landmark
        pass  # TODO


class CreateGameTest(unittest.TestCase):
    def setUp(self):
        self.con = Controller()
        self.Game = game.Game(self.con.System)

    def test_createGame(self):
        lm = ["l1", "l2"]
        tm = ["team1", "team2"]
        self.con.create_game(lm, tm)
        self.assertEqual(self.Game.getLandmarkList(), lm, "Landmarks not created correctly")
        self.assertEqual(self.Game.teams, tm, "Teams not set correctly")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.con = Controller()

    def test_badlogin(self):
        self.con.login("cheater", "sargreat")
        self.assertEqual(self.con.currentUser, None, "Nice try, User scum. Bad username test.")
        self.con.login("admin", "sarpoo")
        self.assertEqual(self.con.currentUser, None, "Nice try, User scum. Bad password test.")

    def test_goodlogin(self):
        self.con.login("admin", "kittens")
        self.assertEqual(self.con.currentUser, "admin", "Admin not successfully logged in.")


class LogoutTest(unittest.TestCase):
    def setUp(self):
        self.con = Controller()
        self.con.username = "admin"

    def test_goodlogout(self):
        self.con.logout()
        self.assertEqual(self.con.currentUser, None, "Current user should be null after logout")


class TestStartGame(unittest.TestCase):
    def setUp(self):
        self.con = Controller()
        self.User = user.User()
        self.User.name = "admin"
        self.Game = game.Game(self.con.System)

    def test_goodstart(self):
        self.con.start_game()
        self.assertTrue(self.Game.isActive, "Game not begun successfully!")

    def test_badStart(self):
        self.Game.isActive = True
        self.con.start_game()
        self.assertTrue(self.Game.isActive, "Calling start game on an active game should do nothing")


class TestEndGame(unittest.TestCase):
    def setUp(self):
        self.con = Controller()
        self.User = user.User()
        self.User.name = "admin"
        self.Game = game.Game(self.con.System)
        self.Game.isActive = True

    def test_endGame(self):
        self.con.end_game()
        self.assertFalse(self.Game.isActive, "End game did not successfully stop the game")

    def test_endGameOnAlreadyEndedGame(self):
        self.Game.isActive = False
        self.con.end_game()
        self.assertFalse(self.Game.isActive, "End game on a non-active game should stay non-active")
