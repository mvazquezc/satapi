import os
from connection import *

class SatAPIRepositories(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Create a repository given a name
    def createRepository(self, Name, Product_Id, Content_Type):
        JSONData=json.dumps(
            {
                'name': Name,
                'product_id': Product_Id,
                'content_type': Content_Type
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'repositories/', JSONData)
        return Response

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
                {'organization_id': Organization['id'],
                 'content_type': Type,
                 'per_page': count})
        return Response

   # Get Satellite Repositories by type and product
    def getRepositoriesByProductType(self, Organization, Type, ProductId,
                                    count=99):
        Response=self.GET(self.KatelloAPILocation + 'repositories',
                   {'organization_id': Organization['id'], 'content_type': Type,
                   'product_id': ProductId, 'per_page': count})
        return Response

    # Get a repository by its name
    def getRepositoryByName(self, Organization, Name):
        Response=self.searchRepository(Organization, 'name = "%s"' % Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # XB Search repository by product_id
    def getRepositoryByGroup(self, Organization, Product_id):
        Response=self.GET(self.KatelloAPILocation + 'repositories',
                          {'organization_id': Organization, 'product_id': Product_id})
        return Response

    # Search repository by a search criteria
    def searchRepository(self, Organization, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'repositories/',
                            {'organization_id': Organization['id'], 'search': criteria, 'count': count, 'per_page': count})
        return Response

    #Sync repository
    def syncRepository(self, RepoId):
        Response = self.POST(self.KatelloAPILocation + 'repositories/' +
        str(RepoId) + '/sync')
        return Response

    # Upload content to Satellite Repository
    def uploadContentToRepository (self, FilePath, RepoId):
	objFile = {'content': (os.path.basename(FilePath), open(FilePath, 'rb'), 'application/octet-stream')}
        Response=self.POST_FILES(self.KatelloAPILocation + 'repositories/' +
                            str(RepoId)+'/upload_content',
                            objFile)

        return Response
