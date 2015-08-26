#!/usr/bin/python -W ignore::DeprecationWarning

import sys
import argparse

from satapi.satapi import SatAPI
from config.config import Config

# Function to print debug messages (-d argument)
def debug(text):
    global args
    if args.debug: print '[DEBUG-MAIN] '+str(text)

# Function to print info messages (-v argument)
def info(text):
    global args
    if args.verbose or args.debug: print '[INFO-MAIN] '+str(text)

# Function to create subnet
def createSubnet(Name, Network, Mask, Gateway, Domain):
    global args, API

    info('Creating %s subnet' % Name)
    subnet=API.createSubnet(Name, Network, Mask, Gateway,
                           args.dns1, args.dns2, 1, Domain)
    debug(subnet)
    debug(subnet['name'])

    info('Attaching %s subnet to %s organization' %
            (subnet['name'], Config.Organization))
    organization=API.getOrganizationByName(Config.Organization)
    debug(API.attachSubnetToOrganization(subnet, organization))
    info('Attaching %s subnet to %s location' %
            (subnet['name'], Config.Location))
    location=API.getLocationByName(Config.Location)
    debug(API.attachSubnetToLocation(subnet, location))

# Main process
def main():
    global args, API

    # Parse command line arguments
    parser=argparse.ArgumentParser(
                description='Script para dar de alta un nuevo centro.'
             )
    parser.add_argument('-c', '--centro',
                help='Numero del centro a dar de alta', required=True)
    parser.add_argument('-e', '--entorno',
                help='Entorno al que pertenece el nuevo centro', required=True)
    parser.add_argument('-dns1', '--dns1',
                help='DNS primario para los equipos', required=False,
                const='8.8.8.8', nargs='?', default='8.8.8.8')
    parser.add_argument('-dns2', '--dns2',
                help='DNS secundario para los equipos', required=False,
                const='4.4.4.4', nargs='?', default='4.4.4.4')
    parser.add_argument('-v', '--verbose',
                help='Muestra informacion del proceso', action='store_true')
    parser.add_argument('-d', '--debug',
                help='Muestra informacion de debug', action='store_true')
    args=parser.parse_args()

    # Create API connector
    API=SatAPI(Config.APILocation,
                 Config.APIUser,
                 Config.APIPassword,
                 args.debug
          )

    # Get domain information
    info('Creating %s.example.com domain' % str(args.centro))
    domain=API.createDomain('%s.example.com' % str(args.centro))
    debug(domain)

    # Get organization information
    info('Getting %s organization information' % Config.Organization)
    organization=API.getOrganizationByName(Config.Organization)
    debug(organization)

    # Get location information
    info('Getting %s location information' % Config.Location)
    location=API.getLocationByName(Config.Location)
    debug(location)

    # Attach Domain to Organization
    info('Attaching %s domain to %s organization' %
            (str(args.centro), Config.Organization))
    debug(API.attachDomainToOrganization(domain, organization))

    # Attach Domain to location
    info('Attaching %s domain to %s location' %
            (str(args.centro), Config.Location))
    debug(API.attachDomainToLocation(domain, location))

    # Set environment
    info('Setting %s environment to domain' % str(args.entorno))
    debug(API.createDomainParameter(domain, 'entorno', str(args.entorno)))

    # Calculate network addres from variable
    network='192.'+str(((int(args.centro)-2000)/256)+224)+'.'
    network+=str((int(args.centro)-2000)%256)

    # Create subnets and attach them to organization and location
    createSubnet('subnet-'+str(args.centro)+'-1',
                    network+'.0', '255.255.255.192', network+'.1',
                    domain['id'])
    createSubnet('subnet-'+str(args.centro)+'-2',
                    network+'.64', '255.255.255.224', network+'.65',
                    domain['id'])
    sys.exit()

if __name__ == '__main__':
    main()
