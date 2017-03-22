from connection import *
import json

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
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

    # Creates config group
    def createConfigGroup(self, config_group={}):
        JSONData = json.dumps(
                {
                    'config_group': config_group
                })

        Response = self.POST(self.SatAPILocation + 'config_groups/', JSONData)
        return Response

    # Updates config group
    def updateConfigGroup(self, id, config_group={}):
        JSONData = json.dumps(
                {
                    'config_group': config_group
                })
        Response = self.PUT(
                self.SatAPILocation + 'config_groups/' + str(id), JSONData)
        return Response
