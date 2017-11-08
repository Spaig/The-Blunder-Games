import landmarks
import unittest
import interface

class System:
    # pseudo database, way to interact with lists
    def __init__(self):
        self.landmarks = []  # [landmark objects]
        #self.users = [User("admin","kittens")] # [user objects] - FOR SPRINT 2
        self.teams = {'admin': "kittens"}  # gamemaker hardcoded - disabled due to user becoming an object(?)

    def addLandmark(self, lm):
        self.landmarks.append(lm)

    def addTeam(self, tm, pw):
      self.teams[tm] = pw


    def getLandmark(self, lm):
        ret = None
        x = 0
        for i in self.landmarks:
          if self.landmarks[x].name == lm:
            return self.landmarks[x]
          x +=1
        print("Invalid landmark")
        return ret

        '''
        try:
            x = self.landmarks.index(lm)
            ret = self.landmarks[x]
        except ValueError:
            print("Invalid landmark")
        return ret
        '''

    def getTeam(self, tm):
        ret = None
        for key in self.teams:
            if tm == key:
                return key
        print("Invalid team name")
        return ret

    def getTeamPassword(self, username):
        ret = None
        try:
          ret = self.teams[username]
        except KeyError:
          print("Invalid username")
        return ret
        '''
        USER OBJECT VERSION OF GETTEAMPASSWORD:
        try:
          for key in self.users:
            if tm == self.users[key].getName():   
                return self.users[key].getPassword
        except KeyError:
          print("Invalid username")
        return ret
        '''

    '''
      
  class TestAddTeam(unittest.TestCase):
    def setUp(self):
      self.Interface = interface.Interface()
      self.User = user.User()
      self.User.currentUser = "admin"   #admin is logged in to make changes
      self.System = System()
    def test_AdminAddTeam(self):
      self.System.addTeam("user","password")
      self.assertEquals(self.System.teams, {"admin":"kittens","user":"password"}, "New user not added correctly")
    def test_NonAdminAdd(self):
      self.User.currentUser = "notadmin"
      self.System.addTeam("user","password")
      self.assertEquals(self.System.teams, {"admin":"kittens"}, "Non-admin user should not be able to add new teams")
  '''
  
class TestAddTeamAcceptance(unittest.TestCase):
    def setUp(self):
      self.Interface = interface.Interface()
      self.System = System()
    def test_AdminAddTeam(self):
      self.Interface.command("CREATEUSER newteam passw0rd")
      self.assertEquals(self.System.teams, {"admin":"kittens","newteam":"passw0rd"}, "New user not added correctly")
      self.Interface.command("CREATEUSER anotherteam wow")
      self.assertEquals(self.System.teams, {"admin":"kittens","newteam":"passw0rd","anotherteam":"wow"}, "New user not added correctly")
