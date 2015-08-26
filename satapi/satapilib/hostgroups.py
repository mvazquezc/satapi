from connection import *

class SatAPIHostgroups(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a hostgroup by its Id number
    def getHostgroup(self, Id):
        Response=self.GET(self.SatAPILocation + 'hostgroups/' + str(Id))
        return Response

    # Get a hostgroup by its name
    def getHostgroupByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'hostgroups/' + Name)
        return Response

    # Search hostgroups by a search criteria
    def searchHostgroup(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'hostgroups/',
                            {'search': criteria, 'count': count})
        return Response
