# -*- coding: utf-8 -*-

"""
@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import sys

# Python 2 compatibility
if sys.version_info[0] == 2:
    # Exceptions for bot
    from exceptions import *

    # Tool for loading plugins and adapters
    from modules import *

    # Tool for loading config from project folder
    from config import *
else:
    # Exceptions for bot
    from .exceptions import *

    # Tool for loading plugins and adapters
    from .modules import *

    # Tool for loading config from project folder
    from .config import *


class Sheldon:
    """
    Main class of the bot.
    Run script creating new instance of this class and run it.
    """

    def __init__(self):
        """
        Function for loading bot.

        :return:
        """

        # Creating empty lists for plugins and adapters
        self.plugins = []
        self.adapters = []

    def load_plugins(self):
        """
        Function for collecting and loading plugins from plugins folder.

        :return:
        """


class Plugin():
    pass
