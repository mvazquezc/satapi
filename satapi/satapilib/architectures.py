from connection import *

class SatAPIArchitectures(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a architecture by its Id number
    def getArchitecture(self, Id):
        Response=self.GET(self.SatAPILocation + 'architectures/' + str(Id))
        return Response


    # Get an architecture by its name
    def getArchitectureByName(self, Name):
        Response=self.searchArchitecture('name="%s"' % Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search architecture by a search criteria
    def searchArchitecture(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'architectures/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response
    
