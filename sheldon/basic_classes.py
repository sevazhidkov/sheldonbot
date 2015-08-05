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
        try:
            self.module.send_message(
                message_text=message.text,

            )


class Message:
    """
    Class for every message: incoming and outcoming.
    """

    def __init__(self, message_text, adapter, message_attachments=[]):
        """
        Init new message

        :param message_text: string, text of new message
        :param adapter: Adapter object, current adapter
        :param message_attachments: list of Attachment objects
        :return:
        """
        self.text = message_text
        self.adapter = adapter
        self.attachments = message_attachments


class Attachment:
    """
    Class for every attachment: incoming and outcoming/
    """

    def __init__(self, attachment_type, attachment_path=None,
                 attachment_text=''):
        """
        Init new attachment.

        :param attachment_type: 'photo', 'video' and other things,
                                supported by adapter
        :param attachment_path: path to photo, video etc.
        :param attachment_text: optional text of attachment - may
                                be сaption or something another
        :return:
        """
        self.type = attachment_type.lower()
        self.path = attachment_path
        self.text = attachment_text

