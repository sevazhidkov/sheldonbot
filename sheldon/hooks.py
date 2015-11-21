# -*- coding: utf-8 -*-

"""
Decorators and other functions for hooks.

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""
import sys
import _thread as thread
import re

from sheldon.exceptions import catch_module_errors


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

    # If not one module return True after check,
    # bot sort matches by priority and choose first.
    priority = 0

    @catch_module_errors
    def call(self, incoming_message, bot):
        """
        Run hook

        :param incoming_message: Message object
        :param bot: Sheldon object
        :return:
        """
        thread.start_new_thread(self.func, (
            incoming_message, bot
        ))


class MessageHook(Hook):
    def __init__(self, user_function, regexes, case_sensitive=False):
        """
        Create new message hook

        :param user_function: decorated user's function, called
                              when regular expression matching with
                              incoming message
        :param regexes: regular expression for messages
        :param case_sensitive: bool, is hook catching messages
                                     with case sensitive
        """
        self.type = 'message'
        self.priority = 3

        self.func = user_function

        if type(regexes) == str:
            regexes = [regexes]
        self.regexes = regexes

        self.case_sensitive = case_sensitive

    def check(self, incoming_message):
        """
        Check, is this message catching for this hook

        :param incoming_message: IncomingMessage object
        :return: True or False
        """
        if not self.case_sensitive:
            for regex in self.regexes:
                if re.match(regex, incoming_message.text, re.IGNORECASE):
                    return True
        else:
            for regex in self.regexes:
                if re.match(regex, incoming_message.text):
                    return True

        return False


class CommandHook(Hook):
    def __init__(self, user_function, command):
        """
        Create new command hook

        :param user_function: decorated user's function, called
                              when command matching with incoming message
        :param command: str, command text without '!'.
                        For example, 'join'.
        """
        self.type = 'command'
        self.priority = 2

        self.func = user_function
        self.command = command

    def check(self, incoming_message):
        """
        Check, is this message catching for this hook

        :param incoming_message: IncomingMessage object
        :return: True or False
        """
        return incoming_message.text.lstrip().startswith('!' + self.command)


class CallbackHook(Hook):
    def __init__(self, user_function, callback_func):
        """
        Create new function hook.

        :param user_function: decorated user's function, called
                              when command matching with incoming message
        :param callback_func: func, that called with incoming_message and
                              it must return True or False
        """
        self.type = 'callback'
        self.priority = 1

        self.func = user_function
        self.callback_func = callback_func

    def check(self, incoming_message):
        """
        Check, is this message catching for this hook

        :param incoming_message: IncomingMessage object
        :return: True or False
        """
        return self.callback_func.__call__(incoming_message)


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


def message(regexes=[], case_sensitive=False):
    """
    Hook for catching messages, for example:
    "i want cat", "thanks" etc.

    :param regexes: list[string], regular expressions for catching messages
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

        wrapped._sheldon_hook = MessageHook(wrapped, regexes, case_sensitive)
        return wrapped

    return hook


def command(command_text):
    """
    Hook for catching commands, for example:
    "!asana", "!deploy sheldon" etc.

    :param command_text: str, command text without '!'. For example, 'join'.
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

        wrapped._sheldon_hook = CommandHook(wrapped, command_text)
        return wrapped

    return hook


def callback(callback_func):
    """
    Hook for catching anything you want, based on
    your callback function

    :param callback_func: callback func, takes incoming message
                          and returns True or False
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

        wrapped._sheldon_hook = CallbackHook(wrapped, callback_func)
        return wrapped

    return hook
