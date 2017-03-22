from connection import *

class SatAPIContentViews(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get a content view by its Id number
    def getContentView(self, Id):
        Response=self.GET(self.KatelloAPILocation + 'content_views/' + str(Id))
        return Response

    # Get content view filters
    def getContentFilters(self, Id):
        Response=self.GET(self.KatelloAPILocation +
                          'content_view_filters/?content_view_id=' +
                          str(Id))
        return Response

    # Get a content view by its name
    # Note: direct URL doesn't work, let's search and return first result only
    def getContentViewByName(self, Name, Organization):
	Response=self.searchContentView(Name, Organization, 1)['results'][0]
        return Response

    # Search content views by a search criteria
    def searchContentView(self, Criteria, Organization, Count=99):
        Response=self.GET(self.KatelloAPILocation + 'content_views/',
                            {'search': Criteria, 'count': Count, 'per_page': Count,
                             'organization_id': Organization['id']})
        return Response

    # Create a content view
    def createContentView(self, Name, OrganizationId, RepositoryIdList = []):
        JSONData=json.dumps(
            {
                'name': Name,
                'repository_ids': RepositoryIdList
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'organizations/' +
                    str(OrganizationId) + '/content_views',
                    JSONData)
        return Response

    # Add a puppet module to a content view
    def addModuleToContentView(self, Module, ContentView):
        JSONData=json.dumps(
            {
                'uuid': Module['id']
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'content_views/' +
                    str(ContentView['id']) + '/content_view_puppet_modules',
                    JSONData)
        return Response

    # Create filter in a content view
    def createFilter(self, Name, ContentView, Inclusion, Type, RepositoryList):
        JSONData=json.dumps(
            {
                'name': Name,
                'content_view_id': ContentView['id'],
                'inclusion': Inclusion,
                'type': Type,
                'repository_ids': RepositoryList
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'content_view_filters',
                    JSONData)
        return Response

    # Add RPM to a CV filter
    def addRuleToContentViewFilter(self, Name, Version, ContentViewFilter):
        JSONData=json.dumps(
            {
                'content_view_filter_id': ContentViewFilter['id'],
                'name': Name,
                'version': Version
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'content_view_filters/' +
                    str(ContentViewFilter['id'])+'/rules',
                    JSONData)
        return Response

    # Publish a new version
    def publishContentView(self, ContentView):
        Response=self.POST(self.KatelloAPILocation + 'content_views/' + 
                    str(ContentView['id'])+'/publish')
        return Response

    # Promote a given CV version id
    def promoteContentViewVersion(self, ContentViewVersion, Environment, Force=False):
        JSONData=json.dumps(
            {
                'environment_id': Environment['id'],
                'force': Force,
            }
        )
        Response=self.POST(self.KatelloAPILocation + 'content_view_versions/' + 
                    str(ContentViewVersion)+'/promote', JSONData)

        return Response

    # Return content view versions
    def getContentViewVersions(self, ContentView):
        Response = self.GET(self.KatelloAPILocation + 'content_views/' +
                            str(ContentView['id']) + '/content_view_versions')
        return Response
