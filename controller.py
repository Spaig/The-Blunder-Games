import unittest, system, user

class Controller:
  def __init__(self):
    self.User = None
    self.Game = None
    self.currentLandmark = None
    self.System = system.System()


  def check(self, parsedText, currentUser): #where parsedText is a list of strings
    #if user=None, don't accept any method except login
    #elif tree of different methods depending on first index of parsedText
    a = eval('A')
    
    pass
  
  #def getInstance(self):
    
  def login(self, username, password):
    pass
  
  def logout(self):
    pass
    
    
    
class LoginTest(unittest.TestCase):
    def setup(self):
      self.User = user.User()
      self.dict = {"admin":"sargreat"}
    def badlogin(self):
       self.assertEqual("Login Failed. Username or password invalid.", self.User.login("cheater", "sargreat"), "Nice try, User scum. Bad username test.")
       self.assertEqual("Login Failed. Username or password invalid.", self.User.login("admin", "sarpoo"), "Nice try, User scum. Bad password test.")
    def goodlogin(self):
       self.assertEqual("Welcome, Admin.", self.User.login("admin"),"Admin not successfully adminned.")
       self.assertEqual("admin", self.User.username,"Current user not set to admin.")
       
class LogoutTest(unittest.TestCase):
    def setup(self):
        self.User = user.User()
        self.username = "admin"
    def goodlogout(self):
        self.User.logout()
        self.assertEqual(self.User.username, None, "Current user should be null after logout")
        
class ToggleTest(unittest.TestCase):
    def setup(self):
        self.User = user.User()
        self.username = "admin"
        self.state = 0
    def goodstart(self):
        self.User.toggle()
        self.assertEqual(self.User.state, 0, "Game not begun successfully!")