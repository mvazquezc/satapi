from connection import *

class SatAPIPTables(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a partition table by its Id number
    def getPTable(self, Id):
        Response=self.GET(self.SatAPILocation + 'ptables/' + str(Id))
        return Response


    # Get a partition table by its name
    def getPTableByName(self, Name):
        Response=self.searchPTable('name="%s"' % Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search ptable by a search criteria
    def searchPTable(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'ptables/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response
    
