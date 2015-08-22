# -*- coding: utf-8 -*-

"""
Decorators and other functions for hooks.

@author: Lises team
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
    def __init__(self, user_function, regex):
        """
        Create new message hook

        :param user_function: decorated user's function, called
                              when regular expression matching with
                              incoming message
        :param regex: regular expression for messages
        """
        self.type = 'message'

        self.func = user_function
        self.regex = regex


def message(regex):
    """
    Hook for catching messages, for example:
    "i want cat", "thanks" etc.

    :param regex: string, regular expression for catching messages
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

        wrapped._sheldon_found = True
        wrapped._sheldon_hook = MessageHook(wrapped, regex)
        return wrapped

    return hook