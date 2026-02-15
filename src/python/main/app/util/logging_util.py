"""
src/python/app/util/logging_util.py
"""

import logging
import time

from app.main.constant import *

log = logging.getLogger( __name__ )

log_message_width = COLUMNS - (23 + 1 + 1 + 1 + 16 + 1 + 1 + 3 + 1)  # 48


def logging_init( logging_level: str = 'INFO' ):
    level = getattr( logging, logging_level )

    formatter = logging.Formatter( datefmt='%Y-%m-%dT%H:%M:%S', fmt='{asctime}.{msecs:0<3.0f} {levelname[0]} {filename:>16}:{lineno:<3}  {message}', style='{' )
    formatter.converter = time.gmtime

    handler = logging.StreamHandler()
    handler.setFormatter( formatter )

    root = logging.getLogger()
    root.addHandler( handler )
    root.setLevel( level )


def log_banner( title: str, columns: int = COLUMNS, output=log.info, character: str = '-' ):
    if output in { log.debug, log.info, log.warning }: columns = log_message_width
    line = int( columns ) * character
    for o in [ '', '', line, f'>>> {title}', line, '' ]:
        output( o )


def log_heading( title: str, columns: int = COLUMNS, output=log.info, character: str = '-' ):
    if output in { log.debug, log.info, log.warning }: columns = log_message_width
    line = str.ljust( f'{title} ', columns, character )
    for o in [ '', '', line, '' ]:
        output( o )
