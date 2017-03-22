from connection import *

class SatAPIOperatingSystems(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a Operating System by its Id number
    def getOperatingSystem(self, Id):
        Response=self.GET(self.SatAPILocation + 'operatingsystems/' + str(Id))
        return Response

    # Get a operatingsystem by its Name
    def getOperatingSystemByName(self, Title):
        Response=self.searchOperatingSystem(Title, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search operatingsystem by a search criteria
    def searchOperatingSystem(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'operatingsystems/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response
    
    # Get OperatingSystem Architectures
    def getOperatingSystemArchitecture(self, OperatingSystem):
        Response=self.GET(self.SatAPILocation + 'operatingsystems/%s/architectures' % OperatingSystem['id'])
        return Response

    # Get OperatingSystem Media
    def getOperatingSystemMedia(self, OperatingSystem):
        Response=self.GET(self.SatAPILocation + 'operatingsystems/%s/media' % OperatingSystem['id'])
        return Response

    # Get OperatingSystem Partition Table
    def getOperatingSystemPartitionTable(self, OperatingSystem):
        Response=self.GET(self.SatAPILocation + 'operatingsystems/%s/ptables' % OperatingSystem['id'])
        return Response
