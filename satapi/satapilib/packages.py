from connection import *

class SatAPIPackages(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a package by its Id number
    def getPackage(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'packages/' + str(Id))
        return Response

    # Get a package by its name
    # Note: direct URL doesn't work, let's search instead and return
    def getPackageByName(self, Name):
        Response=self.searchPackages(Name)
        return Response

    # Search packages by a search criteria
    def searchPackages(self, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'packages/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

