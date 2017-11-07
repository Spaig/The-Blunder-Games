import controller


# if __name__ == '__main__':     This is for things called by import statements

class Interface:
    def __init__(self, c):
        self.Controller = c

    def command(self,
                commandString):  # breaks input into list of commands. list[0] being the action/method to call. Sends list and currentUser to controller class

        if commandString != None:
            commandList = commandString.split()
            return commandList


'''    
class TestCommand(unittest.TestCase):
 def setUp(self):
   pass
 def testParseInput(self):
   self.Interface.command("login admin pass")
   self.assertEquals(parsedList[0], "login", "Should correctly parse for login.")
'''
