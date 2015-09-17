# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

from sheldon import adapter
from sheldon import config
from sheldon import exceptions
from sheldon import manager
from sheldon import storage
from sheldon.utils import logger


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

        self._load_adapter(command_line_arguments)

    def _load_config(self, command_line_arguments):
        """
        Сreate and load bot config.

        :param command_line_arguments: dict, arguments for creating config:
                                       config-prefix - prefix of environment
                                                       variables.
                                                       Default - 'SHELDON_'
        :return:
        """
        if 'config-prefix' in command_line_arguments:
            self.config = config.Config(prefix=command_line_arguments['config-prefix'])
        else:
            self.config = config.Config()

        # If we had problems with config loading, stop the bot.
        if not self.config:
            exit()

    def _load_adapter(self, command_line_arguments={'adapter': 'console'}):
        """
        Load adapter.

        :param command_line_arguments: dict, arguments for creating config:
                                       adapter - name of adapter.
                                                 May be local package in
                                                 adapters folder or package
                                                 from PyPi.
                                                 Default - 'console'.
        :return:
        """
        self.adapter = adapter.load_adapter(command_line_arguments['adapter'])

        # If load adapter function return None, stop the bot.
        if not self.adapter:
            exit()

