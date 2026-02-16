"""
src/python/app/shell/shell.py
"""

import argparse
import logging
import os
import typing

import cmd2
from rich.console import RenderableType

from app.main.dump import dump_rlimit, dump_sysconfig, dump_packages
from app.main.version import VERSION_FULL
from app.util.dict_util import dump_dict
from app.util.process_util import restart_process

log = logging.getLogger( __name__ )


class ApplicationShell( cmd2.Cmd ):

    def __init__( self, cmdline_args: argparse.Namespace = None, /, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.cmdline_args = cmdline_args
        self.prompt = '))) '

    # ---------------------------------------------------------------------------------------------------

    def run( self ):
        self.cmdloop()

    def init( self ):
        ...

    # ---------------------------------------------------------------------------------------------------

    def cmdloop( self, intro: RenderableType = '' ):
        super().cmdloop()

    def onecmd( self, statement, *args, add_to_history=True ):
        return_code = super().onecmd( statement, add_to_history=add_to_history )
        log.debug( f'{return_code=} {statement=}' )
        if return_code:
            return True
        return None

    # ---------------------------------------------------------------------------------------------------

    def do_args( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        dump_dict( 'args', vars( self.cmdline_args ) )

    def do_environment( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        dump_dict( 'environment', os.environ.copy() )

    def do_exit( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        return True

    def do_rlimit( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        dump_rlimit()

    def do_sysconfig( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        dump_sysconfig()

    def do_packages( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        dump_packages()

    def do_restart( self, *args, **kwargs ) -> typing.Optional[ bool ]:
        restart_process()

    def do_version( self, *args, **kwargs ):
        print( f'version is {VERSION_FULL}' )


# ---------------------------------------------------------------------------------------------------

def run_shell( args: argparse.Namespace ):
    shell = ApplicationShell( args )
    shell.run()
