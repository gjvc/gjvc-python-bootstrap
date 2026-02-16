"""
src/python/app/util/dict_util.py
"""

import logging

from app.util.logging_util import log_heading

log = logging.getLogger( __name__ )


def dump_dict( heading: str, d: dict, sort_keys=True ):
    log_heading( heading )
    width = max( [ len( s ) for s in d.keys() ] ) + 2
    keys = sorted( d.keys() ) if sort_keys else d.keys()
    for name in keys:
        value = d[ name ]
        log.info( f'{name:{width}}{value}' )
