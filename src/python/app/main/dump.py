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
    installed_packages = [ d.metadata['Name'] for d in importlib.metadata.distributions() ]

    def get_package_version( name: str ):
        try:
            return importlib.metadata.version( name )
        except importlib.metadata.PackageNotFoundError:
            return None

    version_by_name = { name: get_package_version( name ) for name in installed_packages }
    width = max( [ len( name ) for name in version_by_name.keys() ] ) + 2
    for name, version in version_by_name.items():
        log.info( f'{name:{width}}{version}' )


def dump_sysconfig():
    log_heading( 'sysconfig' )
    width = max( [ len( s ) for s in sysconfig.get_config_vars() ] ) + 2
    for name in sorted( sysconfig.get_config_vars() ):
        value = sysconfig.get_config_vars().get( name )
        log.info( f'{name:{width}}{value}' )


def dump_rlimits():
    log_heading( 'rlimit' )
    names = [ s for s in dir( resource ) if s.startswith( 'RLIMIT_' ) ]
    width = max( [ len( s ) for s in names ] )
    for name in sorted( names ):
        soft, hard = resource.getrlimit( getattr( resource, name ) )
        if soft == -1: soft = 'unlimited'
        if hard == -1: hard = 'unlimited'
        log.info( f'{name:{width}}  {soft:>12}  {hard:>12}' )
