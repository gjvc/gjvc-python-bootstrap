"""
src/python/main/app/main/constant.py
"""

import os


COLUMNS = int( os.environ.get( 'COLUMNS', 80 ) )
ROWS = int( os.environ.get( 'ROWS', 24 ) )

