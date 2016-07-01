import sys
import logging

def setuplogger(debug = False):
    loglevel = 10 if debug else 20

    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%a %d %H:%M:%S',
        level=loglevel
    )

def info(str):
    logging.info(str)

def debug(str):
    logging.debug(str)

def warn(str):
    logging.warn(str)

def error(str):
    logging.error(str)

def info_and_exit(str = 'OK', code = 0):
    logging.info('%s (%d)' % (str, code))
    sys.exit(0)

def error_and_exit(str, code = 255):
    logging.error('KO - %s (%d)' % (str, code))
    sys.exit(code)
