"""
src/python/main/app/main/constant.py
"""

import grp
import os
import pwd

COLUMNS = int( os.environ.get( 'COLUMNS', 80 ) )
ROWS = int( os.environ.get( 'ROWS', 24 ) )

PID = os.getpid()
UID = os.getuid()
GID = os.getgid()
USER = pwd.getpwuid( UID ).pw_name
GROUP = grp.getgrgid( GID ).gr_name
