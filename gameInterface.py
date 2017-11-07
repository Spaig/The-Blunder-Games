import abc


class gameInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getClock(self):
        pass

    @abc.abstractmethod
    def setLandmarkList(self, landmarks):
        pass

    @abc.abstractmethod
    def setTeams(self, teams):  # add existing team to current game?
        pass

    @abc.abstractmethod
    def startClock(self):
        pass

    @abc.abstractmethod
    def stopClock(self):
        pass
