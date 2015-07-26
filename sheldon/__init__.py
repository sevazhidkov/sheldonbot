# -*- coding: utf-8 -*-

"""
@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

__author__ = 'Lises team'
__version__ = '0.1'
__email__ = 'zhidkovseva@gmail.com'

import sys

# Bot file contains bot's main class - Sheldon
# Utils folder contains scripts for more
# comfortable work with sending and parsing
# messages. For example, script for downloading
# files by url.
#
# If bot using Python 2.7 or lower, than we use
# old syntax of importing modules.
# It's needed for Python 2 compatibility

if sys.version_info[0] == 2:
    from bot import *
    from utils import *
else:
    from .bot import *
    from .utils import *