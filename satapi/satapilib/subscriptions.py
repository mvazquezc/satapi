from connection import *

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
