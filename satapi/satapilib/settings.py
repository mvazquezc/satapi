from connection import *

class SatAPISettings(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a setting by its name
    def getSettingByName(self, Name):
        Response=self.GET(self.SatAPILocation + 'settings/', {'search': Name})
        return Response

    # Update a setting
    def updateSetting(self, SettingId, SettingValue):
        JSONData = json.dumps(
                             {
                              'value': SettingValue
                             })
        Response=self.PUT(self.SatAPILocation + 'settings/' + str(SettingId), JSONData)
        return Response
