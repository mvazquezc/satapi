from connection import *

class SatAPIHostcollections(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a host collection by its Id number
    def getHostcollection(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'host_collections/' + str(Id))
        return Response

    # Get a host collection by its name
    def getHostcollectionByName(self, Name):
        Response=self.GET(self.KatelloAPILocation + 'host_collections/',
                            {'name': Name})
        return Response

    # Create a host collection given a name
    def createHostcollection(self, Name, Organization):
        JSONData=json.dumps(
            {
                'name': Name,
                'organization_id': Organization['id'],
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'host_collections/', JSONData)
        return Response

