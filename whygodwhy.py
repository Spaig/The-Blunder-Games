class User:
    # team is treated as individual, will include gamemaker - test!

    def __init__(self):
        self.penalties = 0
        self.timePenalty = 0

    def login(self, username, password):

        pass

    def logout(self, username):
        pass

    def answerQuestion(self, answer):

        # if answer is correct, automatically provide next clue

        pass

    def getQuestion(self):
        pass

    def getStatus(self):
        pass


class Interface:

    def __init__(self):
        pass

    def command(self, commandString):
        pass


class Game:
    def __init__(self):
        self.clock = 0
        self.isActive = False

    def gameStart(self):
        pass

    def gameEnd(self):
        pass

    # holds game landmarks, anything stored within the game


class System:

    # pseudo database, way to interact with lists
    def __init__(self):
        self.landmarks = {}  # {"landmark":[clue, question, answer]}
        self.teams = {"admin": "kittens", }  # gamemaker hardcoded in


'''
speak with the Rock about these
def getLandmark():
pass
def getClue():
pass
def getQuestion():
pass
def getAnswer():
pass
def getTeams():
pass
def setTeams():
pass
'''

'''
Notes for Rock:
what to do for class outlines
TDD?
'''