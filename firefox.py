import configparser
import os

mozilla_profile = os.path.join(os.getenv('APPDATA'), r'Mozilla\Firefox')
mozilla_profile_ini = os.path.join(mozilla_profile, r'profiles.ini')
profile = configparser.ConfigParser()
profile.read(mozilla_profile_ini)
data_path = os.path.normpath(os.path.join(mozilla_profile, profile.get('Profile0', 'Path')))
data_path = os.path.join(data_path, r'cookies.sqlite')

import sqlite3
connection = sqlite3.connect(data_path)
cursor = connection.cursor()
value = cursor.execute('select value from moz_cookies where name = ".ROBLOSECURITY"').fetchone()[0]
print(value)
connection.close()