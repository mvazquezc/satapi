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
    # Note: direct URL doesn't work, let's search and return first result only
    def getEnvironmentByName(self, Name, OrganizationId):
	Response=self.searchEnvironment(Name, OrganizationId, 1)['results'][0]
        return Response

    # Search environments by a search criteria
    def searchEnvironment(self, Criteria, OrganizationId, Count=99):
        Response=self.GET(self.KatelloAPILocation + 'environments/',
                            {'search': Criteria, 'count': Count, 'per_page': Count,
                             'organization_id': OrganizationId})
        return Response
