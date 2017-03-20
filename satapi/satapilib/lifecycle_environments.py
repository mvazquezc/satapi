from connection import *

class SatAPILifecycleEnvironments(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a life cycle environment by its Id number
    def getLifecycleEnv(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'environments/' + str(Id))
        return Response

    # Get a life cycle environment by its name
    def getLifecycleEnvByName(self, Name, Organization):
        Response=self.GET(self.KatelloAPILocation + 'environments',
                            {'name': Name, 'organization_id': Organization['id']})
        return Response

    # Create a life cycle environment given a name
    def createLifecycleEnv(self, Name, Organization, Prior):
        JSONData=json.dumps(
            {
                'name': Name,
                'organization_id': Organization['id'],
                'prior_id': Prior['id'],
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'environments/', JSONData)
        return Response

