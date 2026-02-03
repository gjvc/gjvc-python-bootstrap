"""
src/python/main/main.py
"""

import argparse
import logging
import os

from app.main.dump import dump_rlimits, dump_sysconfig
from app.util.logging_util import logging_init, log_banner, log_heading
from app.util.dict_util import dump_dict

log = logging.getLogger( __name__ )


def announce( args: argparse.Namespace ):
    log_banner( 'app' )


def dispatch( args: argparse.Namespace ):
    if args.args:
        dump_dict( 'args', vars( args ) )
    if args.environment:
        dump_dict( 'environment', os.environ.copy() )
    if args.resource:
        dump_rlimits()
    if args.sysconfig:
        dump_sysconfig()


def parse_args() -> argparse.Namespace:
    logging_level_choices = { 'INFO', 'DEBUG', 'ERROR', 'TRACE', 'FATAL', 'WARNING' }
    logging_level_default = 'INFO'

    _ = argparse.ArgumentParser()
    _.add_argument( '--args', action='store_true' )
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
