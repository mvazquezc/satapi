from connection import *

class SatAPIOrganizations(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get an organization by its Id number
    def getOrganization(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'organizations/' + str(Id))
        return Response

    # Get an organization by its name
    def getOrganizationByName(self, Name):
        Response=self.GET(self.KatelloAPILocation + 'organizations/' + Name)
        return Response
    
    # Create an organization given a name
    def createOrganization(self, Name):
        JSONData=json.dumps(
            {
                'organization': {
                    'name': Name
                }
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'organizations/', JSONData)
        return Response
