from connection import *

class SatAPILocations(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a location by its Id number
    def getLocation(self, Id):
        Response=self.GET(self.SatAPILocation + 'locations/' + str(Id))
        return Response

    # Get a location by its name
    def getLocationByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'locations/' + Name)
        return Response

    # Attach a domain to a location
    def attachDomainToLocation(self, Domain, Location):
        Domains=[Item['id'] for Item in Location['domains'] 
                  if Item['id'] != Domain['id']]
        Domains.append(Domain['id'])

        JSONData=json.dumps(
            {
                'location': {
                    'domain_ids': Domains
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'locations/' + str(Location['id']),
                            JSONData)

        return Response

    # Attach a subnet to an location
    def attachSubnetToLocation(self, Subnet, Location):
        Subnets=[Item['id'] for Item in Location['subnets']
                  if Item['id'] != Subnet['id']]
        Subnets.append(Subnet['id'])

        JSONData=json.dumps(
            {
                'location': {
                    'subnet_ids': Subnets
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'locations/' + str(Location['id']),
                            JSONData)

        return Response
