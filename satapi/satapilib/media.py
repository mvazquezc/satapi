from connection import *

class SatAPIMedia(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get media by its Id number
    def getMedia(self, Id):
        Response=self.GET(self.SatAPILocation + 'media/' + str(Id))
        return Response


    # Get a media by its name
    def getMediaByName(self, Name):
        Response=self.searchMedia('name="%s"' % Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search media by a search criteria
    def searchMedia(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'media/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response
    
