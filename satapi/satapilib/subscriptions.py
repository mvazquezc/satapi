from connection import *
import os

class SatAPISubscriptions(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get subscriptions added to organization
    def getSubscriptions(self, Organization, count=99):
        Response=self.GET(self.KatelloAPILocation + 'organizations/%s/subscriptions' % str(Organization['id']),
			{'count': count, 'per_page': count})
        return Response

    # Search subscriptions by a search criteria
    def searchSubscriptions(self, Organization, criteria, count=99):
        Response=self.GET(self.KatelloAPILocation + 'organizations/%s/subscriptions' % str(Organization['id']),
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

    # Get subscriptions by activation key
    def getSubscriptionsByAK(self, AK_id, count=99):
        Response=self.GET(self.KatelloAPILocation + 'activation_keys/%s/subscriptions' % str(AK_id),
                          {'count': count, 'per_page': count})
        return Response

    # Get subscription manifest history
    def getSubscriptionManifestHistory(self, Organization):
        Response=self.GET(self.KatelloAPILocation + 'organizations/%s/subscriptions/manifest_history' % str(Organization['id']))
        return Response

    # Delete a subscription manifest for a given organization
    def deleteSubscriptionManifest(self, Organization):
        Response=self.POST(self.KatelloAPILocation + 'organizations/%s/subscriptions/delete_manifest' %str(Organization['id']))
        return Response

    def uploadSubscriptionManifest(self, Organization, manifest_zip):
        objFile = {'content': (os.path.basename(manifest_zip), open(manifest_zip, 'rb'), 'application/octet-stream')}
        Response=self.POST_FILES(self.KatelloAPILocation + 'organizations/' +
                   str(Organization['id'])+'/subscriptions/upload', objFile)
        return Response
