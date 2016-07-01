from connection import *

class SatAPIPuppetModules(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a module by its Id number
    def getModule(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'puppet_modules/' + str(Id))
        return Response

    # Get a module by its name
    # Note: direct URL doesn't work, let's search instead and return
    def getModuleByName(self, Name):
        Response=self.searchModules(Name)
        return Response

    # Search mobules by a search criteria
    def searchModules(self, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'puppet_modules/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

