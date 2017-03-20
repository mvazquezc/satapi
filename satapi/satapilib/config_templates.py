from connection import SatAPIConnection

class SatAPIConfigTemplates(SatAPIConnection):
    """Class SatAPIConfigTemplates provides abstraction for configuration
    templates endpoints."""
    def __init__(self, URL, User, Password, Debug=False):
        """Constructor method.

        Args:
            URL: Satellite's URL.
            User: used connecting to Satellite.
            Password: used connecting to Satellite.
            Debug: enable/disable debug logging.
        """
        SatAPIConnection.__init__(self, URL, User, Password, Debug)
        self._base_url = 'config_templates/'

    def getConfigTemplate(self, id):
        """getConfigTemplate fetches a configuration template using the
        given id.

        Args:
            id: Configuration Template ID.
        """
        return self.GET(self.SatAPILocation + self._base_url + str(id))

    def getConfigTemplatesByOrg(self, org_id):
        """getConfigTemplatesByOrg lists all configuration templates given an
        Organization ID.

        Args:
            org_id: Organization ID.
        """
        params = {'organization_id': str(org_id)}
        return self.GET(self.SatAPILocation + self._base_url, params)

    def searchConfigTemplate(self, criteria, count=99):
        """searchConfigTemplate searches configuration templates using the
        given criteria.

        Args:
            criteria: string used to filter results.
            count: number of returned entries per request.
        """
        params = {'search': criteria, 'per_page': count}
        return self.GET(self.SatAPILocation + self._base_url, params)
