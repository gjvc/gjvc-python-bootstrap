"""
src/python/main/app/util/process_util.py
"""

import psutil
import sys
import os

import logging

log = logging.getLogger( __name__ )


def restart_process():
    os.execlp( sys.executable, sys.executable, *sys.argv )
