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

    # Search packages by repo
    def searchPackagesByRepo(self, repoid, count=99):
        Response = self.GET(self.KatelloAPILocation + 'repositories/' +
                            str(repoid) + '/packages', {'per_page': count})
        return Response

    # Search a given package by repoid
    def searchPackageByRepoID(self, repoid, package, count=99):
        """Search a given package on a given repository (ID).

        Args:
            repoid (int): Repository ID.
            package (str): Package name, e.g. 389-ds-base.
            count (int): Number of results per page.
        """
        params = {'search': package, 'per_page': count}
        Response = self.GET(self.KatelloAPILocation + 'repositories/' +
                            str(repoid) + '/packages', params)
        return Response

    # need to get packages using user defined parameters
    def getPackagesByRepoID(self, repoid, params=None):
        Response = self.GET(self.KatelloAPILocation + "repositories/" +
                            str(repoid) + "/packages", params)
        return Response
