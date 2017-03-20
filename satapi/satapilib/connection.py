import json
import sys
import logger as logger
import logging

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

        logger.setuplogger(Debug)

        logging.getLogger("requests").setLevel(logging.CRITICAL)

        # Disable SSL Warnings
        requests.packages.urllib3.disable_warnings()

    def exception(self, text):
        logger.error(str(text))

    # Default methods to do GET/POST/PUT/DELETE actions
    def GET(self, Location, JSON=''):
	logger.debug('ACTION: GET ' + Location)
	logger.debug('PARAMS: ' + str(JSON))
        try:
            Result=requests.get(
    	        Location,
                    params=JSON,
                    auth=(self.APIUser, self.APIPassword),
                    verify=self.SSLVerify)

            logger.debug('RESULT: ' + str(Result))

            Result.raise_for_status()
            logger.debug('RESULT: ' + str(Result.json()))
            return Result.json()
        except Exception as e:
            logger.error(e.message)
            logger.error('Error conectando con Satellite')
            raise

    def POST(self, Location, JSON=''):
	logger.debug('ACTION: POST ' + Location)
	logger.debug('PARAMS: ' + str(JSON))
        try:
            Result=requests.post(
                    Location,
                    data=JSON,
                    auth=(self.APIUser, self.APIPassword),
                    verify=self.SSLVerify,
                    headers=self.POSTHeaders)

            logger.debug('RESULT: ' + str(Result))

            Result.raise_for_status()
            logger.debug('RESULT: ' + str(Result.json()))
            return Result.json()
        except requests.exceptions.HTTPError as e:
            logger.error(e.message)
            logger.error('Error conectando con Satellite')
            logger.debug(Result.url + ': ' +
                         Result.status_code + ' [ ' +
                         Result.reason + ' ]')
            raise

    def POST_FILES(self, Location, FILES):
        logger.debug('ACTION: POST ' + Location)

        try:
            Result=requests.post(
                    Location,
                    files=FILES,
                    auth=(self.APIUser, self.APIPassword),
                    verify=self.SSLVerify)

            logger.debug('RESULT: ' + str(Result))

            Result.raise_for_status()
            logger.debug('RESULT: ' + str(Result.json()))
            return Result.json()
        except requests.exceptions.HTTPError as e:
            logger.error(e.message)
            logger.error_and_exit('Error conectando con Satellite', 4)
            raise


    def PUT(self, Location, JSON=''):
        logger.debug('ACTION: PUT ' + Location)
        logger.debug('PARAMS: ' + str(JSON))
        try:
            Result=requests.put(
                    Location,
                    data=JSON,
                    auth=(self.APIUser, self.APIPassword),
                    verify=self.SSLVerify,
                    headers=self.POSTHeaders)

            logger.debug('RESULT: ' + str(Result))

            Result.raise_for_status()
            logger.debug('RESULT: ' + str(Result.json()))
            return Result.json()
        except requests.exceptions.HTTPError as e:
            logger.error(e.message)
            logger.error('Error conectando con Satellite')
            raise

    def DELETE(self, Location, JSON=''):
        logger.debug('ACTION: DELETE ' + Location)
        logger.debug('PARAMS: ' + str(JSON))
        try:
            Result=requests.delete(
                    Location,
                    data=JSON,
                    auth=(self.APIUser, self.APIPassword),
                    verify=self.SSLVerify,
                    headers=self.POSTHeaders)

            logger.debug('RESULT: ' + str(Result))

            Result.raise_for_status()
            logger.debug('RESULT: ' + str(Result.json()))
            return Result.json()
        except requests.exceptions.HTTPError as e:
            logger.error(e.message)
            logger.error('Error conectando con Satellite', 4)
            raise
