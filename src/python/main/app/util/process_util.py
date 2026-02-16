"""
src/python/main/app/util/process_util.py
"""

import logging
import os
import sys

log = logging.getLogger( __name__ )


def restart_process():
    os.execvpe( sys.executable, [ sys.executable ] + sys.argv, os.environ )
