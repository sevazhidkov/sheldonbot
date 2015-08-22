# -*- coding: utf-8 -*-

"""
Manager for plugins: importing, collecting hooks etc.

@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""


class PluginsManager:
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