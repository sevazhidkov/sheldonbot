# -*- coding: utf-8 -*-

"""
@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import yaml
import os.path



class Adapter():
    """
    Adapter class contains information about adapter:
    name, variables and module using to call adapter methods
    """

    def __init__(self, name, variables):
        """
        Init new Adapter object

        :param name: public name of adapter which used in adapters directory
        :param variables: variables of adapters which set in config file
        """
        self.name = name
        self.variables = variables

        # Load module of adapter later
        self.module = None


def load_adapter_config(config_path, adapter_name):
    """
    Load adapter config with adapter_name from config folder

    :param config_path: string, absolute path to config
                        (not adapters) folder
    :return: Adapter object or None if adapter not found
    """

    adapter_config_path = '{config_folder}/adapters/{adapter}.yml'.format(
        config_folder=config_path, adapter=adapter_name
    )