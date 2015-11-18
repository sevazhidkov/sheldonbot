# -*- coding: utf-8 -*-

"""
Decorators and other functions for hooks.

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import re

from sheldon.exceptions import catch_plugin_errors


class Hook:
    """
    Basic class for hooks
    """
    # Every hook has type. It could be
    # 'command' (command hook), 'message' (message hook),
    # 'interval' (interval hook), 'cron' (cron hook),
    # 'web' (web hook)
    type = ''
    func = None

    @catch_plugin_errors
    def call(self, incoming_message, bot):
        """
        Run hook

        :param incoming_message: Message object
        :param bot: Sheldon object
        :return:
        """
        self.func.__call__(incoming_message, bot)


class MessageHook(Hook):
    def __init__(self, user_function, regex, case_sensitive=False):
        """
        Create new message hook

        :param user_function: decorated user's function, called
                              when regular expression matching with
                              incoming message
        :param regex: regular expression for messages
        :param case_sensitive: bool, is hook catching messages
                                     with case sensitive
        """
        self.type = 'message'

        self.func = user_function
        self.regex = regex
        self.case_sensitive = case_sensitive


def find_hooks(plugin_module):
    """
    Find hooks in plugin module

    :param plugin_module: module object
    :return: list of Hook objects
    """
    hooks = []
    # Iterating throw plugin elements
    for name in plugin_module.__dict__.keys():
        item = plugin_module.__dict__[name]

        # Hooks are setting '_sheldon_hook' parameters
        # on functions when they decorated.
        if hasattr(item, '_sheldon_hook'):
            hooks.append(item._sheldon_hook)
    return hooks


def message(regex, case_sensitive=False):
    """
    Hook for catching messages, for example:
    "i want cat", "thanks" etc.

    :param regex: string, regular expression for catching messages
    :param case_sensitive: bool, is bot catching messages with case sensitive
    :return:
    """

    def hook(func):
        def wrapped(message_object, bot_object):
            """
            Wrapper around user's function

            :param message_object: incoming message, Message object
            :param bot_object: Sheldon object
            :return:
            """
            return func(message_object, bot_object)

        wrapped._sheldon_hook = MessageHook(wrapped, regex, case_sensitive)
        return wrapped

    return hook
