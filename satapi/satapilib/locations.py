from connection import *

class SatAPILocations(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a location by its Id number
    def getLocation(self, Id):
        Response=self.GET(self.SatAPILocation + 'locations/' + str(Id))
        return Response

    # Get a location by its name
    def getLocationByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'locations/' + Name)
        return Response
    
    # Create a location given a name
    def createLocation(self, Name):
        JSONData=json.dumps(
            {
                'location': {
                    'name': Name
                }
            }
        )
        Response=self.POST(self.SatAPILocation + 'locations/', JSONData)
        return Response

