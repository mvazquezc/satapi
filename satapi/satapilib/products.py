from connection import *

class SatAPIProducts(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a product by its name
    def getProductByName(self, Name, Organization):
        Response=self.GET(self.KatelloAPILocation + 'products/', {'name': Name, 'organization_id': Organization['id']})
        return Response

    # Get repository sets from a product
    def getRepositorySetsFromProduct(self, ProductId):
        Response=self.GET(self.KatelloAPILocation + 'products/' + str(ProductId) + '/repository_sets')
        return Response

    def getRepositorySetByName(self, ProductId, Name):
        Response=self.GET(self.KatelloAPILocation + 'products/' + str(ProductId) + '/repository_sets', {'name': Name})
        return Response 

    # Enable repository set from a product
    def enableRepositorySet(self, ProductId, RepositoryId, Basearch=None, Releasever=None):
        JSONData={'basearch': Basearch, 'releasever': Releasever}
        # Remove empty keys from json data, some repos doesn't have releasever or basearch thus the action will fail if those values are sent as None
        JSONData = dict((k, v) for k, v in JSONData.iteritems() if v)
        JSONData = json.dumps(JSONData)
        Response=self.PUT(self.KatelloAPILocation + 'products/' + str(ProductId) + '/repository_sets/' + str(RepositoryId) + '/enable', JSONData)
        return Response

    # Disable repository set from a product
    def disableRepositorySet(self, ProductId, RepositoryId, Basearch=None, Releasever=None):
        JSONData={'basearch': Basearch, 'releasever': Releasever}
        # Remove empty keys from json data, some repos doesn't have releasever or basearch thus the action will fail if those values are sent as None
        JSONData = dict((k, v) for k, v in JSONData.iteritems() if v)
        JSONData = json.dumps(JSONData)
        Response=self.PUT(self.KatelloAPILocation + 'products/' + str(ProductId) + '/repository_sets/' + str(RepositoryId) + '/disable', JSONData)
        return Response

