# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import os


class Config:
    def __init__(self, prefix='SHELDON_'):
        """
        Load config from environment variables.

        :param prefix: string, all needed environment variables
                            starts from it.
                            Default - 'SHELDON_'. So, environment
                            variables will be looking like:
                            'SHELDON_BOT_NAME', 'SHELDON_TWITTER_KEY'
        :return:
        """
        # Bot config variables
        self.variables = {}

        for variable in os.environ:
            if variable.startswith(prefix):
                self.variables[variable] = os.environ[variable]

    def get(self, variable, default_value):
        """

        :param variable: string, needed variable
        :param default_value: string, value that returns if
                              variable is not set
        :return:
        """
        if variable not in self.variables:
            return default_value

        return self.variables[variable]

