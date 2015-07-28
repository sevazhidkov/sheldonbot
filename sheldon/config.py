# -*- coding: utf-8 -*-

"""
@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import yaml

from sheldon.utils import logger


class Adapter():
    """
    Adapter class contains information about adapter:
    name, variables and module using to call adapter methods
    """

    def __init__(self, name, variables):
        """
        Init new Adapter object

        :param name: public name of adapter which used in
                     config/adapters directory
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
    adapter_config = yaml.load(open(adapter_config_path))

    # If config correct, return it.
    # Else - bot can't work correctly.
    if validate_adapter_config(adapter_config_path):
        logger.info_log_message('Loaded config of {name} adapter'.format(
            name=adapter_name
        ))
        return adapter_config
    else:
        error_message = "Can't load config of {name} adapter".format(
            name=adapter_name
        )
        logger.critical_log_message(error_message)
        return None


def validate_adapter_config(config):
    """
    Check required data in adapter config

    :param config: dict, result of yaml.load()
    :return:
    """
    try:
        assert 'name' in config
        # Other validations may be here
        logger.info_log_message('Adapter config is correct')
        return True
    except AssertionError:
        logger.critical_log_message('Incorrect config')
        return False