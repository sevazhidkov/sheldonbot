# -*- coding: utf-8 -*-

"""
Declaration of classes needed for bot working:
Adapter class, Plugin class

@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

from time import sleep


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

    def get_messages(self):
        """
        Get new messages from adapter

        :return: iterator of Message objects
        """
        while True:
            messages = self.module.get_messages()
            for message in messages:
                yield message
            # Sleep seconds, which set in adapter config
            sleep(int(self.variables['timeout']))

    def send_message(self, message):
        """
        Send message with adapter

        :param message: Message object
        :return: True or False - result of sending
        """
        pass


class Message:
    """
    Class for every message: incoming and outcoming.
    """
    def __init__(self, message_text, adapter):
        self.text = message_text
        self.adapter = adapter

