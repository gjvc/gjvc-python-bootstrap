"""
src/python/main/app/main/constant.py
"""

import grp
import os
import pwd

COLUMNS: int = int( os.environ.get( 'COLUMNS', 80 ) )
ROWS: int = int( os.environ.get( 'ROWS', 24 ) )

GID: int = os.getgid()
GROUP: str = grp.getgrgid( GID ).gr_name

UID: int = os.getuid()
USER: str = pwd.getpwuid( UID ).pw_name

PID: int = os.getpid()
