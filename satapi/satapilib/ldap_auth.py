from connection import *

class SatAPILdapAuth(SatAPIConnection):
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)

    # Get all ldap auth sources
    def getLdapAuthSources(self):
        Response=self.GET(self.SatAPILocation + 'auth_source_ldaps/')
        return Response

    # Crete a new ldap auth source
    def createLdapAuthSource(self, Name, Host, Port=None, Account=None, BaseDN=None, AccountPassword=None, AttrLogin=None,
                             AttrFirstName=None, AttrLastName=None, AttrMail=None, AttrPhoto=None, OntheflyRegister=None,
                             UsergroupSync=None, Tls=None, GroupsBase=None, ServerType=None, LdapFilter=None, 
                             LocationIds=None, OrganizationIds=None):
        JSONData=json.dumps(
            {
                'auth_source_ldap': {
                    'name': Name,
                    'host': Host,
                    'port': Port,
                    'account': Account,
                    'base_dn': BaseDN,
                    'account_password': AccountPassword,
                    'attr_login': AttrLogin,
                    'attr_firstname': AttrFirstName,
                    'attr_lastname': AttrLastName,
                    'attr_mail': AttrMail,
                    'attr_photo': AttrPhoto,
                    'onthefly_register': OntheflyRegister,
                    'usergroup_sync': UsergroupSync,
                    'tls': Tls,
                    'groups_base': GroupsBase,
                    'server_type': ServerType,
                    'ldap_filter': LdapFilter,
                    'location_ids': LocationIds,
                    'organization_ids': OrganizationIds
                }
            }
        )
        Response=self.POST(self.SatAPILocation + 'auth_source_ldaps/', JSONData)
        return Response

