# -*- coding: utf-8 -*-

"""
Functions and classes for adapter working

@author: Lises team
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
    Class for every attachment: incoming and outcoming
    """

    def __init__(self, attachment_type, attachment_path=None,
                 attachment_text=''):
        """
        Init new attachment.

        :param attachment_type: 'photo', 'video', 'link'
                                and other things, supported by adapter
        :param attachment_path: path to photo, video, url etc.
        :param attachment_text: optional text of attachment - may
                                be сaption or something another
        :return:
        """
        self.type = attachment_type.lower()
        self.path = attachment_path
        self.text = attachment_text


def load_adapter(config):
    adapter_name = config.get('SHELDON_ADAPTER_NAME', required=True)
    try:
        adapter_module = import_module('adapters.{}'.format(
            config.get('SHELDON_ADAPTER_NAME')
        ))
    except ImportError as error:
        logger.critical_log_message("Error while loading plugin: \n" +
                                    str(error.__traceback__))
        return None
    adapter_module.on_start()
    adapter_object = Adapter(adapter_name,
                             adapter_module)
    return adapter_object
