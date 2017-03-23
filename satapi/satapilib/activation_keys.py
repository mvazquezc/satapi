from connection import *

class SatAPIActivationKeys(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get an activation key by its Id number
    def getActivationKey(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'activation_keys/' + str(Id))
        return Response

    # Get an activation key by its name
    def getActivationKeyByName(self, Name, Organization):
        params = {'name': Name, 'organization_id': Organization.get('id')}
        Response=self.GET(self.KatelloAPILocation + 'activation_keys/', params)
        return Response

    # Create Activation Key
    def createActivationKey(self, Name, Organization, Environment, ContentView):
        JSONData=json.dumps(
            {
                'name': Name,
                'organization_id': Organization['id'],
                'environment_id': Environment['id'],
                'content_view_id': ContentView['id'],
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'activation_keys',
                            JSONData)
        return Response

    # Change the release in an Activation Key
    def setActivationKeyRelease(self, ActivationKey, Release):
        JSONData=json.dumps(
            {
                'release_version': Release
            }
        )
        Response=self.PUT(self.KatelloAPILocation + 'activation_keys/' +
                            str(ActivationKey['id']), JSONData)
        return Response

    # Attach subscriptions to an Activation Key
    def setActivationKeySubscriptions(self, ActivationKey, Subscriptions):
        JSONData=json.dumps(
            {
                'id': ActivationKey['id'],
                'subscriptions': Subscriptions
            }
        )
        Response=self.PUT(self.KatelloAPILocation + 'activation_keys/' +
                            str(ActivationKey['id']) + '/add_subscriptions',
                            JSONData)
        return Response

    # Attach Host collections to an Activation Key
    def setActivationKeyHostCollections(self, ActivationKey, Hostcollections):
        JSONData=json.dumps(
            {
                'id': ActivationKey['id'],
                'host_collection_ids': Hostcollections
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'activation_keys/' +
                            str(ActivationKey['id']) + '/host_collections',
                            JSONData)
        return Response

    # Override a product (enable/disable) in an Activation Key
    def overrideActivationKeyProduct(self, ActivationKey, Name, Enable):
        JSONData=json.dumps(
            {
                'content_override': {
                    'content_label': Name,
                    'name': 'enabled',
                    'value': Enable
                }
            }
        )
        Response=self.PUT(self.KatelloAPILocation + 'activation_keys/' +
                            str(ActivationKey['id']) + '/content_override',
                            JSONData)
        return Response
