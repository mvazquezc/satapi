from satapilib import *

class SatAPI(SatAPIDomains, 
             SatAPIEnvironments,
             SatAPIHosts,
	     SatAPIHostgroups,
             SatAPILocations,
             SatAPIOrganizations,
             SatAPISubnets):

    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIDomains.__init__(self, URL, User, Password, Debug)
        SatAPIEnvironments.__init__(self, URL, User, Password, Debug)
        SatAPIHosts.__init__(self, URL, User, Password, Debug)
        SatAPIHostgroups.__init__(self, URL, User, Password, Debug)
        SatAPILocations.__init__(self, URL, User, Password, Debug)
        SatAPIOrganizations.__init__(self, URL, User, Password, Debug)
        SatAPISubnets.__init__(self, URL, User, Password, Debug)
