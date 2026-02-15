"""
src/python/main/app/action/restart.py
"""

import psutil
import logging

log = logging.getLogger( __name__ )


def do_restart( *args, **kwargs ):
    log.debug( 'restart' )
    # psutil.exec()
