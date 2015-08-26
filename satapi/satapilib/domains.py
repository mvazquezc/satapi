from connection import *

class SatAPIDomains(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a domain by its Id number
    def getDomain(self, Id):
        Response=self.GET(self.SatAPILocation + 'domains/' + str(Id))
        return Response

    # Get a domain by its name
    def getDomainByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'domains/' + Name)
        return Response

    # Create a domain
    def createDomain(self, Name):
        JSONData=json.dumps(
            {
                'domain': {
                    'name': Name
                }
            }
        )
        Response=self.POST(self.SatAPILocation + 'domains/', JSONData)
        return Response
        
    # Delete a domain
    def deleteDomain(self, Domain):
        Response=self.DELETE(self.SatAPILocation + 'domains/' + 
                                str(Domain['id']))
	return Response

    # Create a new parameter in a domain
    def createDomainParameter(self, Domain, Name, Value):
        JSONData=json.dumps(
            {
                'parameter': {
                    'name': Name,
                    'value' : Value
                }
            }
        )
        Response=self.POST(self.SatAPILocation + 'domains/' + str(Domain['id'])+
                            '/parameters', JSONData)

        return Response
    
    # Modify an existing parameter in a domain
    def setDomainParameter(self, Domain, Name, Value):
        for Parameter in Domain['parameters']:
            if Parameter['name']==Name:
                Parameter['value']=Value 

        JSONData=json.dumps(
            {
                'domain': {
                    'domain_parameters_attributes': Domain['parameters']
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'domains/' + str(Domain['id']),
                            JSONData)

        return Response
