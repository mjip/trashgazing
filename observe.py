#!/usr/bin/env python3

from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv
from sgp4.ext import jday
from geocart import geo2cart, cart2geo

import os
import getpass
from datetime import datetime

satellites = []

def download_tle():
    space_track_username = input('Enter your space-track username: ')
    space_track_password = getpass.getpass('Enter your space-track password: ')
    if not (space_track_username and space_track_password):
        print('Username and password cannot be blank')
        exit(1)
    shell_command_get_cookies = 'curl -c cookies.txt -b cookies.txt ' +             \
        'https://www.space-track.org/ajaxauth/login -d "identity={}&password={}"'   \
        .format(space_track_username, space_track_password)
    shell_command_get_tle = 'curl --cookie cookies.txt ' +          \
            'https://www.space-track.org/basicspacedata/query/' +   \
            'class/tle_latest/OBJECT_TYPE/DEBRIS/' +                \
            'orderby/ORDINAL%20asc/limit/65000/format/tle/' +       \
            'emptyresult/show > tle.txt'
    os.system(shell_command_get_cookies)
    os.system(shell_command_get_tle)

def load_tle_data():
    now = datetime.now()
    with open('tle.txt', 'r') as f:
        while True:
            try:
                line1 = f.readline()
                line2 = f.readline()
                debris = twoline2rv(line1, line2, wgs84)
                position, velocity = debris.propagate(
                    now.year, now.month, now.day, now.hour+1)
                d = {
                    'satellite' : debris,
                    'position'  : position,
                    'velocity'  : velocity
                }
                satellites.append(d)
            except:
                return

def get_current_location():
    pass

def find_nearby_debris(current_location: tuple):
    '''
    This function takes a tuple of x,y,z coordinates of current location,
    and return a list of nearby 'visible' debris
    '''

#download_tle()
#load_tle_data()
#print(satellites)
#print(len(satellites))
