from connection import *

class SatAPIConfigGroups(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a config group by its Id number
    def getConfigGroup(self, Id):
        Response=self.GET(self.SatAPILocation + 'config_groups/' + str(Id))
        return Response

    # Get a config group by its name
    # Note: direct URL doesn't work, let's search and return first result only
    def getConfigGroupByName(self, Name):
	Response=self.searchConfigGroup(Name)['results'][0]
        return Response

    # Search config groups by a search criteria
    def searchConfigGroup(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'config_groups/',
                            {'search': criteria, 'count': count})
        return Response

