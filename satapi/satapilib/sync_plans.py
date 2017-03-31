from connection import *

class SatAPISyncPlans(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a sync plan by its name
    def getSyncPlanByName(self, Name, Organization):
        Response=self.GET(self.KatelloAPILocation + 'sync_plans/', {'name': Name, 'organization_id': Organization['id']})
        return Response
    
    # Create a sync plan
    def createSyncPlan(self, Name, Organization, Interval, SyncDate, Description=None, Enabled=False):
        JSONData=json.dumps(
            {
                'name': Name,
                'organization_id': Organization['id'],
                'interval': Interval,
                'sync_date': SyncDate,
                'description': Description,
                'enabled': Enabled
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'organizations/' +
                    str(Organization['id']) + '/sync_plans', JSONData)
        return Response
 
    # Add products to a sync plan
    def addProductToSyncPlan(self, Organization, SyncPlan, Products):
        JSONData=json.dumps(
            {
                'id': SyncPlan['id'],
                'product_ids': Products
            }
        )
        Response=self.PUT(self.KatelloAPILocation + 'organizations/' +
                            str(Organization['id']) + '/sync_plans/' +
                            str(SyncPlan['id']) + '/add_products', JSONData)
        return Response

