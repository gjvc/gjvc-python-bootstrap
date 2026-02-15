"""
src/python/app/main/main.py
"""

import argparse
import datetime
import grp
import logging
import os
import pwd

from app.main.dump import dump_rlimit, dump_sysconfig, dump_packages
from app.shell.shell import run_shell
from app.util.dict_util import dump_dict
from app.util.logging_util import logging_init, log_banner, log_heading

log = logging.getLogger( __name__ )


def announce( args: argparse.Namespace ):
    now = datetime.datetime.now().isoformat()
    PID = os.getpid()
    UID = os.getuid()
    GID = os.getgid()
    USER = pwd.getpwuid( UID ).pw_name
    GROUP = grp.getgrgid( GID ).gr_name
    log_banner( f'app starting at {now}, PID {PID}, UID {UID} ({USER}), GID {GID} ({GROUP})' )


def dispatch( args: argparse.Namespace ):
    if args.args:
        dump_dict( 'args', vars( args ) )
    if args.environment:
        dump_dict( 'environment', os.environ.copy() )
    if args.resource:
        dump_rlimit()
    if args.sysconfig:
        dump_sysconfig()
    if args.packages:
        dump_packages()

    if not any( { args.args, args.environment, args.resource, args.sysconfig, args.packages } ):
        run_shell( args )


def parse_args() -> argparse.Namespace:
    logging_level_choices = { 'INFO', 'DEBUG', 'ERROR', 'TRACE', 'FATAL', 'WARNING' }
    logging_level_default = 'INFO'

    _ = argparse.ArgumentParser()
    _.add_argument( '--args', action='store_true' )
    _.add_argument( '--packages', action='store_true' )
    _.add_argument( '--environment', action='store_true' )
    _.add_argument( '--resource', action='store_true' )
    _.add_argument( '--sysconfig', action='store_true' )
    _.add_argument( '--logging-level', choices=logging_level_choices, default=logging_level_default )
    return _.parse_args()


def main():
    args = parse_args()
    logging_init( args.logging_level )

    announce( args )
    dispatch( args )


if __name__ == '__main__':
    main()
