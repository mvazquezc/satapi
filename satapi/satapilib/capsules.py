from connection import *

class SatAPICapsules(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a capsule by its Id number
    def getCapsule(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'capsules/' + str(Id))
        return Response

    # Get a capsule by its name
    def getCapsuleByName(self, Name):
        Response=self.searchCapsule('name="%s"' % Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search capsule by a search criteria
    def searchCapsule(self, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'capsules/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response
   
    # Synchronize a capsule
    def syncCapsule(self, Id):
        Response=self.POST(self.KatelloAPILocation + 'capsules/%s/content/sync' %str(Id))
        return Response

    # Set Capsule Locations
    def setCapsuleLocations(self, Id, LocationsIds):
        JSONData=json.dumps(
            {
                'smart_proxy': {
                    'location_ids': LocationsIds
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'smart_proxies/' + str(Id), JSONData)
        return Response
    
    # Set Capsule organizations
    def setCapsuleOrganizations(self, Id, OrganizationIds):
        JSONData=json.dumps(
            {
                'smart_proxy': {
                    'organization_ids': OrganizationIds
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'smart_proxies/' + str(Id), JSONData)
        return Response

    # Get Capsule lifecycle environment
    def getCapsuleLifecycleEnv(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'capsules/' + 
                    str(Id) + '/content/lifecycle_environments')
        return Response

    # Set Capsule lifecycle environment
    def setCapsuleLifecycleEnv(self, Id, EnvironmentId):
        JSONData=json.dumps(
            {
                'environment_id': EnvironmentId
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'capsules/' +
                    str(Id) + '/content/lifecycle_environments', JSONData)
        return Response

