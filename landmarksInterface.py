import abc


class landmarksInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setClue(self, clue):  # to be called by gamemaker
        pass

    @abc.abstractmethod
    def setQuestion(self, question):  # to be called by gamemaker
        pass

    @abc.abstractmethod
    def setAnswer(self, answer):  # to be called by gamemaker
        pass
