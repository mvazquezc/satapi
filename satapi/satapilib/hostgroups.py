from connection import *

class SatAPIHostgroups(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a hostgroup by its Id number
    def getHostgroup(self, Id):
        Response=self.GET(self.SatAPILocation + 'hostgroups/' + str(Id))
        return Response

    # Get a hostgroup by its name
    def getHostgroupByName(self, Name):
        Response=self.searchHostgroup(Name, 1)
        try:
            return Response['results'][0]
        except:
            return False

    # Search hostgroups by a search criteria
    def searchHostgroup(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'hostgroups/',
                            {'search': criteria, 'count': count})
        return Response

    # Create a hostgroup
    def createHostgroup(self, Name, Parent=None):
        if Parent is None:
            JSONData=json.dumps(
                {
                    'name': Name,
                }
            )
        else:
            JSONData=json.dumps(
                {
                    'hostgroup': {
                        'name': Name,
                        'parent_id': Parent['id']
                    }
                }
            )

        Response=self.POST(self.SatAPILocation + 'hostgroups', JSONData)
        return Response

    # Attach a hostgroup to an organization
    def attachHostgroupToOrganization(self, Hostgroup, Organization):
        JSONData=json.dumps(
            {
                'hostgroup': {
                    'organization_ids': [
                        str(Organization['id']),
                    ],
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hostgroups/' + 
                            str(Hostgroup['id']), JSONData)

        return Response

    # Attach a hostgroup to a location
    def attachHostgroupToLocation(self, Hostgroup, Location):
        JSONData=json.dumps(
            {
                'hostgroup': {
                    'location_ids': [
                        str(Location['id']),
                    ],
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hostgroups/' + 
                            str(Hostgroup['id']), JSONData)

        return Response

    # Set the content (content view/environment) of a hostgroup
    def setHostgroupContent(self, Hostgroup, ContentView, Environment):
        JSONData=json.dumps(
            {
                'hostgroup': {
                    'content_view_id': ContentView['id'],
                    'lifecycle_environment_id': Environment['id'],
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hostgroups/' + 
                            str(Hostgroup['id']), JSONData)

        return Response

    # Set the puppet environment of a hostgroup
    def setHostgroupPuppetEnvironment(self, Hostgroup, PuppetEnvironment):
        JSONData=json.dumps(
            {
                'hostgroup': {
                    'environment_id': PuppetEnvironment['id'],
                    'environment_name': PuppetEnvironment['name'],
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hostgroups/' + 
                            str(Hostgroup['id']), JSONData)

        return Response

    # Set the operating system information of a hostgroup
    def setHostgroupOperatingSystem(self, Hostgroup, OperatingSystem,
        Architecture, Medium, PartitionTable, Password):
        JSONData=json.dumps(
            {
                'hostgroup': {
                    'operatingsystem_id': OperatingSystem['id'],
                    'operatingsystem_name': OperatingSystem['name'],
                    'architecture_id': Architecture['id'],
                    'architecture_name': Architecture['name'],
                    'medium_id': Medium['id'],
                    'medium_name': Medium['name'],
                    'ptable_id': PartitionTable['id'],
                    'ptable_name': PartitionTable['name']
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hostgroups/' + 
                           str(Hostgroup['id']), JSONData)

        return Response

    # Add Smart Parameter to a hostgroup
    def setHostgroupParameter(self, Hostgroup, Name, Value):
        JSONData=json.dumps(
            {
                'hostgroup_id': Hostgroup['id'],
                'parameter': {
                    'name': Name,
                    'value': Value
                }
            }
        )
        Response=self.POST(self.SatAPILocation + 'hostgroups/' +
                            str(Hostgroup['id'])+'/parameters',
                            JSONData)

        return Response

    # Set Puppet Classes to a hostgroup
    def setHostgroupPuppetClassesIds(self, Hostgroup, Ids):
        JSONData=json.dumps(
            {
                'hostgroup': {
                    'puppetclass_ids': Ids,
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hostgroups/' +
                            str(Hostgroup['id']), JSONData)

        return Response
