from connection import *
import logger as logger

class SatAPIPuppetClasses(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a class by its Id number
    def getPuppetClass(self, Id):
        Response=self.GET(self.SatAPILocation + 'puppetclasses/' + str(Id))
        return Response

    # Get a class by its name
    def getPuppetClassByName(self, Name):
        #Response=self.GET(self.SatAPILocation + 'puppetclasses/' + str(Name))
        criteria = "name = %s" % Name
        Response=self.searchPuppetClasses(criteria)
        return Response

    # Search classes by a search criteria
    def searchPuppetClasses(self, criteria, count=99):
        Response=self.GET(self.SatAPILocation + 'puppetclasses/',
                            {'search': criteria, 'count': count, 'per_page': count})
        return Response

    # Create override order for a given class parameter
    def setPuppetClassSmartParameterOverridesOrder(self, PuppetClass,
            Parameter, OverridesOrder):
        Response=self.PUT(self.SatAPILocation + 'puppetclasses/' +
                            PuppetClass + '/smart_class_parameters/' +
                            Parameter, OverridesOrder)
        return Response

    # Get overrides for a given class parameter
    def getPuppetClassSmartParameterOverrides(self, PuppetClass, Parameter):
        JSONData={
                'count': 999,
                'per_page': 999
            }
        Response=self.GET(self.SatAPILocation + 'puppetclasses/' +
                            PuppetClass + '/smart_class_parameters/' +
                            Parameter + '/override_values', JSONData)
        return Response

    # Set/update override values for a given class parameter
    def setPuppetClassSmartParameterOverrides(self, PuppetClass,
        Parameter, OverridesJSON):
        try:
            Response=self.POST(self.SatAPILocation + 'puppetclasses/' +
                            PuppetClass + '/smart_class_parameters/' +
                            Parameter + '/override_values', OverridesJSON)
        except:
            Response=self.getPuppetClassSmartParameterOverrides(PuppetClass,
                            Parameter)

            try:
                OverridesJSON=json.loads(OverridesJSON)
                for NewOverride in OverridesJSON['override_value']:
                    found=False
                    for ExistingOverride in Response['results']:
                        if ExistingOverride['match'] == NewOverride['match']:
                            found=True
                            logger.debug('Updating existing override matching %s with id %s' %
                                (ExistingOverride['match'],ExistingOverride['id']))
                            ResponsePUT=self.PUT(self.SatAPILocation + 'puppetclasses/' +
                                PuppetClass + '/smart_class_parameters/' +
                                Parameter + '/override_values/' + str(ExistingOverride['id']),
                                json.dumps(NewOverride))
                    if found == False:
                        ResponsePOST=self.POST(self.SatAPILocation + 'puppetclasses/' +
                            PuppetClass + '/smart_class_parameters/' +
                            Parameter + '/override_values', json.dumps({'override_value': NewOverride}))
            except requests.exceptions.HTTPError as e:
                 self.exception(e.message)
                 Response = 0
        return Response

    #Method for fetching smart_class_params with all atributes
    def getSmartClassParameter(self, sp_id):
        """
        Args:
            sp_id (int): smart class parameter id
        """

        try:
            Response = self.GET(self.SatAPILocation +
                                "smart_class_parameters/" +
                                str(sp_id))
        except Exception as err:
            raise err

        return Response
    
    # Get all smart class parameters
    def getSmartClassParameters(self, count=99):
        Response=self.GET(self.SatAPILocation + 'smart_class_parameters', {'count': count, 'per_page': count})
        return Response
    
    # Get overrides for a Smart Clss Prameters
    def getSmartClassParameterOverride(self, Parameter, count=99):
        Response=self.GET(self.SatAPILocation + 'smart_class_parameters/' + str(Parameter) + '/override_values', {'count': count, 'per_page': count})
        return Response
    
    # Delete overrides from a Smart Class Parameter
    def deleteSmartClassSmartParameterOverrides(self, Parameter, Override):
        Response=self.DELETE(self.SatAPILocation + 'smart_class_parameters/' + str(Parameter) + '/override_values/' + str(Override))
	return Response
