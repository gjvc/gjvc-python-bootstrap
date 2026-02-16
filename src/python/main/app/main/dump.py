"""
src/python/main/main.py
"""

import importlib.metadata
import logging
import resource
import sysconfig

from app.util.logging_util import log_heading

log = logging.getLogger( __name__ )


def dump_packages():
    installed_packages = [ d.metadata[ 'Name' ] for d in importlib.metadata.distributions() ]

    def get_package_version( name: str ):
        try:
            return importlib.metadata.version( name )
        except importlib.metadata.PackageNotFoundError:
            return None

    version_by_name = { name: get_package_version( name ) for name in installed_packages }
    width = max( [ len( name ) for name in version_by_name.keys() ] ) + 2
    log_heading( 'packages' )
    for name in sorted( version_by_name.keys(), key=lambda s: str.lower( s ) ):
        version = version_by_name[ name ]
        log.info( f'{name:{width}}{version}' )


def dump_sysconfig():
    width = max( [ len( s ) for s in sysconfig.get_config_vars() ] ) + 2
    log_heading( 'sysconfig' )
    for name in sorted( sysconfig.get_config_vars() ):
        value = sysconfig.get_config_vars().get( name )
        log.info( f'{name:{width}}{value}' )


def dump_rlimit():
    names = [ s for s in dir( resource ) if s.startswith( 'RLIMIT_' ) ]
    width = max( [ len( s ) for s in names ] )
    log_heading( 'rlimit' )
    log.info( f'{"NAME":{width}}  {"SOFT":>12}  {"HARD":>12}' )
    for name in sorted( names ):
        soft, hard = resource.getrlimit( getattr( resource, name ) )
        if soft == -1: soft = 'unlimited'
        if hard == -1: hard = 'unlimited'
        log.info( f'{name:{width}}  {soft:>12}  {hard:>12}' )
