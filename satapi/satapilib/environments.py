from connection import *

class SatAPIEnvironments(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a environment by its Id number
    def getEnvironment(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'environments/' + str(Id))
        return Response

    # Get a environment by its name
    def getEnvironmentByName(self, Name):
        Response=self.GET(self.KatelloAPILocation + 'environments/' + Name)
        return Response

    # Search environments by a search criteria
    def searchEnvironment(self, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'environments/',
                            {'search': criteria, 'count': count})
        return Response
