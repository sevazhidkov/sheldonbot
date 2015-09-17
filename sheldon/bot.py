# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

from sheldon.exceptions import *
from sheldon.manager import *
from sheldon.config import *
from sheldon.adapter import *
from sheldon.storage import *


class Sheldon:
    """
    Main class of the bot.
    Run script creating new instance of this class and run it.
    """

    def __init__(self, command_line_arguments):
        """
        Function for loading bot.

        :param command_line_arguments: dict, arguments for start script
        :return:
        """

        self._load_config(command_line_arguments)

    def _load_config(self, command_line_arguments):
        """
        Сreate and load bot config.

        :param command_line_arguments: dict, arguments for creating config:
                                       config-prefix - prefix of environment
                                                       variables.
                                                       Default - 'SHELDON_'
        :return:
        """
        # Config class is imported from sheldon.config
        if 'config-prefix' in command_line_arguments:
            self.config = Config(prefix=command_line_arguments['config-prefix'])
        else:
            self.config = Config()
