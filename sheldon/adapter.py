# -*- coding: utf-8 -*-

"""
Functions and classes for adapter working

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

from importlib import import_module
from time import sleep

from sheldon.utils import logger


class Adapter:
    """
    Adapter class contains information about adapter:
    name, variables and module using to call adapter methods.
    All adapters inherited from Adapter class'
    """

    def __init__(self, name, module):
        """
        Init new Adapter object

        :param name: public name of adapter which used in
                     config/adapters directory
        :param variables: variables of adapters which set
                          in os.environ or in config.py.
                          Example of adapter variable - Slack API key.
        :param module: imported adapter's module
        """
        self.name = name
        self.module = module


class Message:
    """
    Class for every message: incoming and outcoming.
    """

    def __init__(self, message_text, message_attachments, channel=None, variables={}):
        """
        Create new message.

        :param message_text: string, text of message
        :param message_attachments: list[Attachment] or Attachment object,
                                    attachments with message
        :param channel: Message's channel: channel in Slack, room in Hipchat etc.
        :param variables: dict, external parameters from/to adapter:
                          may be 'slack_username', 'slack_emoji', 'telegram_id'
                          Read about those in adapters' documentation.
                          Parameters should start from adapter name.
        """
        self.message_text = message_text
        # If attachment only one, convert it to list
        if type(message_attachments) == Attachment:
            self.message_attachments = [message_attachments]
        else:
            self.message_attachments = message_attachments
        self.channel = channel
        self.variables = variables


class IncomingMessage(Message):
    """
    Class for messages from user.
    """

    def __init__(self, sender, *args, **kwargs):
        """
        Create new message from user.

        :param sender: User object, sender of message
        """
        super().__init__(*args, **kwargs)
        self.sender = sender


class OutgoingMessage(Message):
    """
    Class for messages from bot.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Attachment:
    """
    Class for every attachment: incoming and outcoming
    """

    def __init__(self, attachment_type, attachment_path=None,
                 attachment_text='', attachment_id=None):
        """
        Init new attachment.

        :param attachment_type: 'photo', 'video', 'link'
                                and other things, supported by adapter
        :param attachment_path: path to photo, video, url etc.
        :param attachment_text: optional text of attachment - may
                                be сaption or something another
        :param attachment_id: int, not required id of attachment from adapter
        :return:
        """
        self.type = attachment_type.lower()
        self.path = attachment_path
        self.text = attachment_text
        self.id = attachment_id


def load_adapter(bot):
    adapter_name = bot.config.get('SHELDON_ADAPTER_NAME', required=True)
    try:
        adapter_module = import_module('adapters.{}'.format(
            bot.config.get('SHELDON_ADAPTER_NAME')
        ))
    except ImportError as error:
        logger.critical_log_message("Error while loading plugin: \n" +
                                    str(error.__traceback__))
        return None
    adapter_module.on_start(bot)
    adapter_object = Adapter(adapter_name,
                             adapter_module)
    return adapter_object
