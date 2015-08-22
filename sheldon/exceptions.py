# -*- coding: utf-8 -*-

"""
Tools for catching exceptions

@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

from sheldon.utils import logger


def catch_plugin_errors(plugin_call_function):
    """
    Catch all plugin exceptions and log it

    :param plugin_call_function: function with calling user plugin
    :return:
    """
    def wrapper(*args, **kwargs):
        try:
            plugin_call_function(*args, **kwargs)
        except Exception as error:
            error_message = str(error.__traceback__)
            logger.error_log_message('Plugin error: \n' + error_message)

    return wrapper
