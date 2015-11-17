from satapilib import *

class SatAPI(SatAPIActivationKeys,
             SatAPIConfigGroups,
             SatAPIContentViews,
             SatAPIDomains, 
             SatAPIEnvironments,
             SatAPIHosts,
	     SatAPIHostgroups,
             SatAPILocations,
             SatAPIOrganizations,
             SatAPIPuppetClasses,
             SatAPIPuppetModules,
             SatAPIPuppetEnvironments,
             SatAPISubnets):

    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIActivationKeys.__init__(self, URL, User, Password, Debug)
        SatAPIConfigGroups.__init__(self, URL, User, Password, Debug)
        SatAPIContentViews.__init__(self, URL, User, Password, Debug)
        SatAPIDomains.__init__(self, URL, User, Password, Debug)
        SatAPIEnvironments.__init__(self, URL, User, Password, Debug)
        SatAPIHosts.__init__(self, URL, User, Password, Debug)
        SatAPIHostgroups.__init__(self, URL, User, Password, Debug)
        SatAPILocations.__init__(self, URL, User, Password, Debug)
        SatAPIOrganizations.__init__(self, URL, User, Password, Debug)
        SatAPIPuppetClasses.__init__(self, URL, User, Password, Debug)
        SatAPIPuppetEnvironments.__init__(self, URL, User, Password, Debug)
        SatAPIPuppetModules.__init__(self, URL, User, Password, Debug)
        SatAPISubnets.__init__(self, URL, User, Password, Debug)
