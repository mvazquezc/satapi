from connection import *

class SatAPICapsules(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a capsule by its Id number
    def getCapsule(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'capsules/' + str(Id))
        return Response


    # Get a capsule by its name
    def getCapsuleByName(self, Name):
        Response=self.searchCapsule('name="%s"' % Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search capsule by a search criteria
    def searchCapsule(self, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'capsules/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response
    
