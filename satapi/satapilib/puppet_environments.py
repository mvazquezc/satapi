from connection import *

class SatAPIPuppetEnvironments(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a puppet environment by its Id number
    def getPuppetEnvironment(self, Id):
        Response=self.GET(self.SatAPILocation + 'environments/' + str(Id))
        return Response

    # Get a puppet environment by its name
    # Note: direct URL doesn't work, let's search and return first result only
    def getPuppetEnvironmentByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'environments/' + Name)
        return Response
