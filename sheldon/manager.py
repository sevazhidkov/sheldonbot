# -*- coding: utf-8 -*-

"""
Manager for plugins: importing, collecting hooks etc.

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import importlib


class PluginsManager:
    def __init__(self):
        """
        Create plugins manager
        :return:
        """
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
    except ImportError:
        return None