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

    ##THE ~FUTURE~ @abc.abstractmethod
    ##THE ~FUTURE~ def startClock(self):
     ##THE ~FUTURE~    pass

    ##THE ~FUTURE~ @abc.abstractmethod
    ##THE ~FUTURE~ def stopClock(self):
    ##THE ~FUTURE~     pass
