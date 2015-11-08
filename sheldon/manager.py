# -*- coding: utf-8 -*-

"""
Manager for plugins: importing, collecting hooks etc.

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import os
import importlib

from sheldon.utils import logger


class PluginsManager:
    def __init__(self, config):
        """
        Create plugins manager

        :param config: Config object with bot information
        :return:
        """
        self.config = config

    def load_plugins(self):
        """
        Load plugins from 'installed_plugins.txt' file

        :return: list of modules
        """
        plugin_names = config.get_installed_plugins()
        plugins = []
        for plugin_name in plugin_names:
            plugin = import_plugin(plugin_name)
            if plugin is not None:
                plugins.append(plugin)
        return plugins

    def reload_plugins(self):
        # TODO
        pass


class Plugin:
    def __init__(self, name, module, hooks):
        """
        Create new plugin

        :param name: string, module name
        :param module: module, imported plugin module
        :param hooks: list of Hook objects
        :return:
        """
        self.name = name
        self.module = module
        self.hooks = hooks


def import_plugin(plugin_name):
    """
    Import plugin using importlib

    :param plugin_name: full name of plugin, ex. 'plugins.console'
    :return: module object or None if plugin not found
    """
    try:
        return importlib.import_module(plugin_name)
    except ImportError as error:
        logger.error_message('Error with loading {}: \n {}'.format(
            plugin_name, error.__traceback__
        ))
        return None
