from connection import *

class SatAPISubnets(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a subnet by its Id number
    def getSubnet(self, Id):
        Response=self.GET(self.SatAPILocation + 'subnets/' + str(Id))
        return Response

    # Get a subnet by its name
    def getSubnetByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'subnets/' + Name)
        return Response

    # Create a new subnet
    def createSubnet(self, Name, Network, Mask, Gateway, DNSServer1, DNSServer2,
                     TFTPServer, Domain):
        JSONData=json.dumps(
            {
                'subnet': {
                    'name': Name,
                    'tftp_id': TFTPServer,
                    'dns_primary': DNSServer1,
                    'dns_secondary': DNSServer2,
                    'domain_ids': Domain,
                    'network': Network,
                    'mask': Mask,
                    'gateway': Gateway
                }
            }
        )

        Response=self.POST(self.SatAPILocation + 'subnets/', JSONData)

        return Response

    # Remove a domains attached to a subnet
    def detachDomainFromSubnet(self, DomainId, SubnetId):
        Response=self.GET(self.SatAPILocation + 'subnets/' + str(SubnetId))
        Domains = [Domain['id'] for Domain in Response['domains'] 
                    if Domain['id'] != DomainId]

        JSONData=json.dumps(
            {
                'subnet': {
                    'domain_ids': Domains
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'subnets/' + str(SubnetId),
                            JSONData)

        return Response

    # Delete a subnet
    def deleteSubnet(self, Subnet):
        Response=self.DELETE(self.SatAPILocation + 'subnets/' + str(Subnet['id']))
	return Response

    # Attach a subnet to an organization
    def attachSubnetToOrganization(self, Subnet, Organization):
        JSONData=json.dumps(
            {
                'subnet': {
                    'organization_ids': [
                        str(Organization['id']),
                    ],
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'subnets/' + str(Subnet['id']),
                            JSONData)

        return Response

    # Attach a subnet to a location
    def attachSubnetToLocation(self, Subnet, Location):
        JSONData=json.dumps(
            {
                'subnet': {
                    'location_ids': [
                        str(Location['id']),
                    ],
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'subnets/' + str(Subnet['id']),
                            JSONData)

        return Response
