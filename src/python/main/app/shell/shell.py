"""
src/python/app/shell/shell.py
"""

import argparse
import logging
import os

import cmd2

from app.main.dump import dump_rlimit, dump_sysconfig, dump_packages
from app.util.dict_util import dump_dict
from app.util.process_util import restart_process

log = logging.getLogger( __name__ )


class ApplicationShell( cmd2.Cmd ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.prompt = '))) '

    def init( self ):
        ...

    def cmdloop( self ):
        super().cmdloop()

    def onecmd( self, statement, *args, add_to_history=True ):
        return_code = super().onecmd( statement, add_to_history=add_to_history )
        log.debug( f'{return_code=} {statement=}' )
        if return_code is True:
            return True
        return None

    # ---------------------------------------------------------------------------------------------------

    def do_version( self, *args, **kwargs ):
        print( f'version is ...' )

    def do_quit( self, *args, **kwargs ):
        print( f'about to quit ...' )
        self.stop = True
        return True

    # ---------------------------------------------------------------------------------------------------

    def do_args( self, *args, **kwargs ):
        dump_dict( 'args', vars( args ) )

    def do_environment( self, *args, **kwargs ):
        dump_dict( 'environment', os.environ.copy() )

    def do_rlimit( self, *args, **kwargs ):
        dump_rlimit()

    def do_sysconfig( self, *args, **kwargs ):
        dump_sysconfig()

    def do_packages( self, *args, **kwargs ):
        dump_packages()

    def do_restart( self, *args, **kwargs ):
        restart_process()

    # ---------------------------------------------------------------------------------------------------

    def run( self, args: argparse.Namespace ):
        self.cmdloop()


# ---------------------------------------------------------------------------------------------------

def run_shell( args: argparse.Namespace ):
    shell = ApplicationShell()
    shell.run( args )
