import abc


class userInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def answer_question(self, answer):
        pass

    @abc.abstractmethod
    def get_question(self):
        pass

    @abc.abstractmethod
    def get_status(self):
        pass

    @abc.abstractmethod
    def create_game(self, landmark, teams):
        pass

    @abc.abstractmethod
    def start_game(self):
        pass

    @abc.abstractmethod
    def end_game(self):
        pass

    @abc.abstractmethod
    def create_landmark(self, name, clue, question, answer):
        pass
