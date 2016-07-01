from connection import *

class SatAPISystems(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a system by its UUID number
    def getSystem(self, Uuidd):
        Response=self.GET(self.KatelloAPILocation + 'systems/' + str(Uuidd))
        return Response

    # Get a system by its name
    def getSystemByName(self, Name):
        Response=self.GET(self.KatelloAPILocation + 'systems/',
                            {'name': Name})
        try:
            return Response['results'][0]
        except:
            return False

    # Search systems by a search criteria
    def searchSystem(self, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'systems',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

    # Edit a system
    def editSystem(self, Uuid, Data):
        Response=self.PUT(self.KatelloAPILocation + 'systems/' + str(Uuid),
                            json.dumps(Data))
        return Response

