from connection import *

class SatAPIHosts(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a host by its Id number
    def getHost(self, Id):
        Response=self.GET(self.SatAPILocation + 'hosts/' + str(Id))
        return Response

    # Get a host by its name
    def getHostByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'hosts/' + Name)
        return Response

    # Search hosts by a search criteria
    def searchHost(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'hosts',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

    # Edit a host
    def editHost(self, Id, Data):
        Response=self.PUT(self.SatAPILocation + 'hosts/' + str(Id),
                            json.dumps(Data))

        return Response

    # Enable/Disable build mode
    def setBuildMode(self, Id, Status):
        Response=self.PUT(self.SatAPILocation + 'hosts/' + str(Id), 
                            json.dumps({'host': {'build': Status}}))
	return Response

    # Modify an existing parameter in a host
    def setHostParameter(self, Host, Name, Value):
        for Parameter in Host['parameters']:
            if Parameter['name']==Name:
                Parameter['value']=Value 

        JSONData=json.dumps(
            {
                'host': {
                    'host_parameters_attributes': Host['parameters']
                }
            }
        )
        Response=self.PUT(self.SatAPILocation + 'hosts/' + str(Host['id']),
                            JSONData)

        return Response

    # Get a host by its name
    def getHostFactsByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'hosts/' + Name + '/facts',
                             {'per_page': 99999})
        return Response['results'][Name]
    
    # Delete a Host
    def deleteHost(self, Host):
        Response=self.DELETE(self.SatAPILocation + 'hosts/' + 
                                str(Host['id']))
        return Response

