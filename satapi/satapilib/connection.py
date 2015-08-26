import json
import sys

try:
    import requests
except ImportError:
    print 'Please install the python-requests module.'
    sys.exit(-1)

class SatAPIConnection:
    # URL definitions
    APILocation=None
    SatAPILocation=None
    KatelloAPILocation=None

    # User and password to authenticate
    APIUser=None
    APIPassword=None

    # Other connection details
    SSLVerify=False
    POSTHeaders={
        'content-type': 'application/json',
        'accept': 'application/json;version=2'
    }
    Debug=False
    
    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        self.APILocation=URL
        self.SatAPILocation='%s/api/v2/' % URL
        self.KatelloAPILocation='%s/katello/api/v2/' % URL
        self.APIUser=User
        self.APIPassword=Password
        self.Debug=Debug

    # Debug messages
    def debug(self, text):
        if self.Debug: print '[DEBUG-SATAPI] '+str(text)

    # Default methods to do GET/POST/PUT/DELETE actions
    def GET(self, Location, JSON=''):
        Result=requests.get(
	        Location, 
                params=JSON, 
                auth=(self.APIUser, self.APIPassword), 
                verify=self.SSLVerify)

        self.debug(str(Result))
        try:
            Result.raise_for_status()
            return Result.json()
        except requests.exceptions.HTTPError as e:
            sys.exit('[EXCEPTION-SATAPI] ' + e.message)

    def POST(self, Location, JSON=''):
        Result=requests.post(
                Location,
                data=JSON,
                auth=(self.APIUser, self.APIPassword),
                verify=self.SSLVerify,
                headers=self.POSTHeaders)

        self.debug(str(Result))
        try:
            Result.raise_for_status()
            return Result.json()
        except requests.exceptions.HTTPError as e:
            sys.exit('[EXCEPTION-SATAPI] ' + e.message)

    def PUT(self, Location, JSON=''):
        Result=requests.put(
                Location,
                data=JSON,
                auth=(self.APIUser, self.APIPassword),
                verify=self.SSLVerify,
                headers=self.POSTHeaders)

        self.debug(str(Result))
        try:
            Result.raise_for_status()
            return Result.json()
        except requests.exceptions.HTTPError as e:
            sys.exit('[EXCEPTION-SATAPI] ' + e.message)

    def DELETE(self, Location, JSON=''):
        Result=requests.delete(
                Location,
                data=JSON,
                auth=(self.APIUser, self.APIPassword),
                verify=self.SSLVerify,
                headers=self.POSTHeaders)

        self.debug(str(Result))
        try:
            Result.raise_for_status()
            return Result.json()
        except requests.exceptions.HTTPError as e:
            sys.exit('[EXCEPTION-SATAPI] ' + e.message)
