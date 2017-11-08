import unittest
from landmarksInterface import landmarksInterface


class Landmarks(landmarksInterface):
    def __init__(self, name, clue, question, answer):
        self.name = name
        self.clue = clue
        self.question = question
        self.answer = answer
    
    def getName(self):
        return self.name
    
    def setClue(self, clue):  # to be called by gamemaker
        self.clue = clue

    def getClue(self):
        return self.clue

    def setQuestion(self, question):  # to be called by gamemaker
        self.question = question

    def getQuestion(self):
        return self.question

    def setAnswer(self, answer):  # to be called by gamemaker
        self.answer = answer
        
    def getAnswer(self):
        return self.answer


class TestSetClue(unittest.TestCase):
    def setUp(self):
        self.Landmark = Landmarks("Central Park", "Near the dumpster", "What is the meaning of the universe?",
                                  "The guy right behind you")

    def test_normalSetClue(self):
        self.assertEqual(self.Landmark.clue, "Near the dumpster", "Clue is incorrect to start")
        self.Landmark.setClue("So many tests")
        self.assertEqual(self.Landmark.clue, "So many tests", "Clue not changed on call to setClue()")


class TestGetClue(unittest.TestCase):
    def setUp(self):
        self.Landmark = Landmarks("Central Park", "Near the dumpster", "What is the meaning of the universe?",
                                  "The guy right behind you")

    def test_getClue(self):
        self.assertEqual(self.Landmark.getClue(), "Near the dumpster", "Clue is not correct")


class TestGetQuestion(unittest.TestCase):
    def setUp(self):
        self.Landmark = Landmarks("Central Park", "Near the dumpster", "What is the meaning of the universe?",
                                  "The guy right behind you")

    def test_getQuestion(self):
        self.assertEqual(self.Landmark.getQuestion(), "What is the meaning of the universe?",
                         "GetQuestion() returns incorrect question")


class TestSetQuestion(unittest.TestCase):
    def setUp(self):
        self.Landmark = Landmarks("Central Park", "Near the dumpster", "What is the meaning of the universe?",
                                  "The guy right behind you")

    def test_normalSetQuestion(self):
        self.Landmark.setQuestion("Who wrote the declaration of independence?")
        self.assertEqual(self.Landmark.question, "Who wrote the declaration of independence?",
                         "Question not set correctly after call to setQuestion()")


class TestSetAnswer(unittest.TestCase):
    def setUp(self):
        self.Landmark = Landmarks("Central Park", "Near the dumpster", "What is the meaning of the universe?",
                                  "The guy right behind you")

    def test_normalSetAnswer(self):
        self.Landmark.setAnswer("Bologna")
        self.assertEqual(self.Landmark.answer, "Bologna", "Answer not set correctly after call to setAnswer()")
