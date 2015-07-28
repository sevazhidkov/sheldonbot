# -*- coding: utf-8 -*-

"""
@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import yaml

from sheldon.utils import logger


class Adapter:
    """
    Adapter class contains information about adapter:
    name, variables and module using to call adapter methods
    """

    def __init__(self, name, variables):
        """
        Init new Adapter object

        :param name: public name of adapter which used in
                     config/adapters directory
        :param variables: variables of adapters which set in config file.
                          Example of adapter variable - Slack API key.
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
    try:
        adapter_config = yaml.load(open(adapter_config_path))
    except FileNotFoundError:
        logger.critical_log_message('Config of {} adapter is not found'.format(
            adapter_name
        ))
        return None

    # If config correct, return it.
    # Else - bot can't work correctly.
    if validate_config(adapter_config, 'adapter', ['name']):
        logger.info_log_message('Loaded config of {name} adapter'.format(
            name=adapter_name
        ))

        # Delete 'name' field to set 'variables' parameter of Adapter object.
        # If config == {name: 'lulz', slack_api: 123} than variables param
        # must be just {slack_api: 123}
        adapter_config.pop('name')

        # Creating new Adapter object
        adapter = Adapter(adapter_name, adapter_config)
        return adapter_config
    else:
        error_message = "Can't load config of {name} adapter".format(
            name=adapter_name
        )
        logger.critical_log_message(error_message)
        return None


def validate_config(config, config_type, required_fields):
    """
    Check that config of config_type contains required fields.
    For example, adapter config must contain 'name' field.

    :param config: dict, result of yaml.load()
    :param config_type: string, 'adapter'/'plugin'/'general'
    :param required_fields: list of strings
    :return:
    """
    try:
        # Check, that config contains all required fields
        for field in required_fields:
            assert field in config

        logger.info_log_message('{} config is correct'.format(config_type))
        return True
    except AssertionError:
        logger.critical_log_message('Incorrect {} config'.format(config_type))
        return False