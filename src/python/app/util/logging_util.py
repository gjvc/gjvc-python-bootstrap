"""
src/python/app/util/logging_util.py
"""

import logging
import time

log = logging.getLogger( __name__ )


def logging_init( logging_level='INFO' ):
    logging.basicConfig(
        datefmt='%Y-%m-%dT%H:%M:%S',
        format='{asctime}.{msecs:0<3.0f} {levelname[0]} {filename:>16}:{lineno:<3}  {message}',
        level=logging.INFO,
        style='{'
    )

    logging_level = getattr( logging, logging_level )
    logging.Formatter.converter = time.gmtime
    logging.getLogger().setLevel( logging_level )


def log_banner( title: str, width: int = 99, output=log.info, character='-' ):
    line = width * character
    for o in [ '', '', line, title, line, '' ]:
        output( o )


def log_heading( title: str, width: int = 99, output=log.info, character='-' ):
    line = str.ljust( f'{title} ', width, character )
    for o in [ '', '', line, '' ]:
        output( o )
