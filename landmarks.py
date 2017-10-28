class Landmarks:
    def __init__(self, name, clue, question, answer):
      self.name = name
      self.clue = clue
      self.question = question
      self.answer = answer
      
    def setClue(self, clue): #to be called by gamemaker
      self.clue = clue
      
    def setQuestion(self, question): #to be called by gamemaker
      self.question = question
      
    def setAnswer(self, answer): #to be called by gamemaker
      self.answer = answer