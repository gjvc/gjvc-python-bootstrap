"""
src/python/app/util/logging_util.py
"""

import logging
import time

from app.main.constant import COLUMNS

log = logging.getLogger( __name__ )

log_message_width = COLUMNS - (23 + 1 + 1 + 1 + 16 + 1 + 1 + 3 + 1)  # 48


def logging_init( logging_level: str = 'INFO' ):
    level = getattr( logging, logging_level )

    addLoggingLevel( 'TRACE', logging.DEBUG - 5 )

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


def addLoggingLevel( levelName: str, levelNum: int, methodName=None ):
    if not methodName:
        methodName = levelName.lower()

    if hasattr( logging, levelName ):
        raise AttributeError( f'{levelName} already defined in logging module' )
    if hasattr( logging, methodName ):
        raise AttributeError( f'{methodName} already defined in logging module' )
    if hasattr( logging.getLoggerClass(), methodName ):
        raise AttributeError( f'{methodName} already defined in logger class' )

    def logForLevel( self, message, *args, **kwargs ):
        if self.isEnabledFor( levelNum ):
            self._log( levelNum, message, args, **kwargs )

    def logToRoot( message, *args, **kwargs ):
        logging.log( levelNum, message, *args, **kwargs )

    logging.addLevelName( levelNum, levelName )
    setattr( logging, levelName, levelNum )
    setattr( logging.getLoggerClass(), methodName, logForLevel )
    setattr( logging, methodName, logToRoot )
