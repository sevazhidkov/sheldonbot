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

        :param prefix: str, all needed environment variables
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

