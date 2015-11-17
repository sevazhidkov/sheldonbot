# -*- coding: utf-8 -*-

"""
Manager for plugins: importing, collecting hooks etc.

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import importlib

from sheldon.utils import logger
from sheldon.hooks import find_hooks


class PluginsManager:
    def __init__(self, config):
        """
        Create plugins manager

        :param config: Config object with bot information
        :return:
        """
        self.config = config
        self.plugins = []

    def load_plugins(self):
        """
        Load plugins from 'installed_plugins.txt' file

        :return: list of Plugin objects
        """
        plugin_names = self.config.installed_plugins
        for plugin_name in plugin_names:
            self._load_plugin(plugin_name)

    def reload_plugins(self):
        # TODO
        pass

    def _load_plugin(self, plugin_name):
        """
        Parse config, find hooks and create new Plugin object.

        :param plugin_name: name for plugin import
        :return:
        """
        plugin_module = import_plugin(plugin_name)
        if not plugin_module:
            logger.error_message("'{}' plugin didn't load".format(
                plugin_name
            ))
            return
        hooks = find_hooks(plugin_module)

        plugin = Plugin(plugin_name, plugin_module, hooks)
        self.plugins.append(plugin)


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
