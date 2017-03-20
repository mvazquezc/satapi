from satapilib import *

class SatAPI(SatAPIActivationKeys,
             SatAPIArchitectures,
             SatAPICapsules,
             SatAPIConfigGroups,
             SatAPIContentViews,
             SatAPIDomains,
             SatAPIEnvironments,
             SatAPIHosts,
             SatAPIHostcollections,
             SatAPIHostgroups,
             SatAPILifecycleEnvironments,
             SatAPILocations,
             SatAPIMedia,
             SatAPIOperatingSystems,
             SatAPIOrganizations,
             SatAPIPackages,
             SatAPIPTables,
             SatAPIPuppetClasses,
             SatAPIPuppetModules,
             SatAPIPuppetEnvironments,
             SatAPIRepositories,
             SatAPISubnets,
             SatAPISubscriptions,
             SatAPISystems,
             SatAPITasks,
             SatAPIConfigTemplates):

    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIActivationKeys.__init__(self, URL, User, Password, Debug)
        SatAPIArchitectures.__init__(self, URL, User, Password, Debug)
        SatAPICapsules.__init__(self, URL, User, Password, Debug)
        SatAPIConfigGroups.__init__(self, URL, User, Password, Debug)
        SatAPIConfigTemplates.__init__(self, URL, User, Password, Debug)
        SatAPIContentViews.__init__(self, URL, User, Password, Debug)
        SatAPIDomains.__init__(self, URL, User, Password, Debug)
        SatAPIEnvironments.__init__(self, URL, User, Password, Debug)
        SatAPIHosts.__init__(self, URL, User, Password, Debug)
        SatAPIHostcollections.__init__(self, URL, User, Password, Debug)
        SatAPIHostgroups.__init__(self, URL, User, Password, Debug)
        SatAPILifecycleEnvironments.__init__(self, URL, User, Password, Debug)
        SatAPILocations.__init__(self, URL, User, Password, Debug)
        SatAPIMedia.__init__(self, URL, User, Password, Debug)
        SatAPIOperatingSystems.__init__(self, URL, User, Password, Debug)
        SatAPIOrganizations.__init__(self, URL, User, Password, Debug)
        SatAPIPackages.__init__(self, URL, User, Password, Debug)
        SatAPIPTables.__init__(self, URL, User, Password, Debug)
        SatAPIPuppetClasses.__init__(self, URL, User, Password, Debug)
        SatAPIPuppetEnvironments.__init__(self, URL, User, Password, Debug)
        SatAPIPuppetModules.__init__(self, URL, User, Password, Debug)
        SatAPIRepositories.__init__(self, URL, User, Password, Debug)
        SatAPISubnets.__init__(self, URL, User, Password, Debug)
        SatAPISubscriptions.__init__(self, URL, User, Password, Debug)
        SatAPISystems.__init__(self, URL, User, Password, Debug)
        SatAPITasks.__init__(self, URL, User, Password, Debug)
