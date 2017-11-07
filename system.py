class System:
    # pseudo database, way to interact with lists
    def __init__(self):
        self.landmarks = []  # [landmark objects]
        self.teams = {"admin": "kittens"}  # gamemaker hardcoded in

    def getLandmarks(self):
        return self.landmarks

    def getTeams(self):
        return self.teams

    def getTeamPassword(self, username):
        try:
            ret = self.teams[username]
        except KeyError:
            print("Invalid username")
        return ret

    '''def addTeam(self, username, password): #need to check if User.currentUser = "admin", if not don't do anything
      pass
      
      
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
  
  
  DON'T NEED ACCEPTANCE YET
  class TestAddTeamAcceptance(unittest.TestCase):
    def setUp(self):
      self.User = user.User()
      self.Interface = interface.Interface()
      self.User.currentUser = "admin"
      self.System = System()
    def test_AdminAddTeam(self):
      self.Interface.command("addTeam(\"newuser\",\"newpass\")")
      self.assertEquals(self.System.teams, {"admin":"kittens","newuser":"newpass"}, "New user not added correctly")
    def test_NonAdminAddTeam(self):
      self.User.currentUser = "notadmin"
      self.Interface.command("addTeam(\"newuser\",\"newpass\")")
      self.assertEquals(self.System.teams, {"admin":"kittens"}, "Non-admin user should not be able to add new teams")
  '''
