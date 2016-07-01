import os
from connection import *

class SatAPIRepositories(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a repository by its Id number
    def getRepository(self, Id, Organization):
        Response=self.GET(self.KatelloAPILocation + 'repositories/' + str(Id),
                          {'organization_id': Organization['id']})
        return Response

    # Get Satellite Repositories
    def getRepositories(self, Organization, count=99):
        Response=self.GET(self.KatelloAPILocation + 'repositories',
		{'organization_id': Organization['id'], 'per_page': count})
        return Response

    # Get Satellite Repositories by type
    def getRepositoriesByType(self, Organization, Type, count=99):
        Response=self.GET(self.KatelloAPILocation + 'repositories',
                {'organization_id': Organization['id'], 'content_type': Type, 'per_page': count})
        return Response

    # Get a repository by its name
    def getRepositoryByName(self, Organization, Name):
        Response=self.searchRepository(Organization, 'name="%s"' % Name, 1)

        try:
            return Response['results'][0]
        except:
            return False

    # Search repository by a search criteria
    def searchRepository(self, Organization, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'repositories/',
                            {'organization_id': Organization['id'], 'search': criteria, 'count': count, 'per_page': count})
        return Response


    # Upload content to Satellite Repository
    def uploadContentToRepository (self, FilePath, RepoId):

	objFile = {'content': (os.path.basename(FilePath), open(FilePath, 'rb'), 'application/octet-stream')}
        Response=self.POST_FILES(self.KatelloAPILocation + 'repositories/' +
                            str(RepoId)+'/upload_content',
                            objFile)

        return Response
