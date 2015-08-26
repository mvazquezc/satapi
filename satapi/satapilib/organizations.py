from connection import *

class SatAPIOrganizations(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get an organization by its Id number
    def getOrganization(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'organizations/' + str(Id))
        return Response

    # Get an organization by its name
    def getOrganizationByName(self, Name):
        Response=self.GET(self.KatelloAPILocation + 'organizations/' + Name)
        return Response

    # Attach a domain to an organization
    def attachDomainToOrganization(self, Domain, Organization):
        Domains=[Item['id'] for Item in Organization['domains'] 
                  if Item['id'] != Domain['id']]
        Domains.append(Domain['id'])

        JSONData=json.dumps(
            {
                'organization': {
                    'domain_ids': Domains
                }
            }
        )
        Response=self.PUT(self.KatelloAPILocation + 'organizations/' + str(Organization['id']),
                            JSONData)

        return Response

    # Attach a subnet to an organization
    def attachSubnetToOrganization(self, Subnet, Organization):
        Subnets=[Item['id'] for Item in Organization['subnets'] 
                  if Item['id'] != Subnet['id']]
        Subnets.append(Subnet['id'])

        JSONData=json.dumps(
            {
                'organization': {
                    'subnet_ids': Subnets
                }
            }
        )
        Response=self.PUT(self.KatelloAPILocation + 'organizations/' + str(Organization['id']),
                            JSONData)

        return Response
