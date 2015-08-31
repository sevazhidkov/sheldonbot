# -*- coding: utf-8 -*-

"""
Interface to Redis-storage.

@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""
from .utils import logger

# We will catch all import exceptions in bot.py
from redis import StrictRedis


class Storage:
    def __init__(self, bot):
        """
        Create new storage for bot

        :param bot: Bot object
        :return:
        """
        self.bot = bot

        # Connect to Redis.
        # If we had problems with Redis - just set self.redis to None.
        # Not redis-required modules must work without Redis.
        try:
            self.redis = StrictRedis(host=bot.config.get('SHELDON_REDIS_HOST',
                                                         'localhost'),
                                     port=int(
                                         bot.config.get('SHELDON_REDIS_PORT',
                                                        '6379')
                                     ),
                                     db=int(
                                         bot.config.get('SHELDON_REDIS_DB', '0')
                                     )
                                    )
        except Exception as error:
            logger.error_log_message('Error while connection Redis:')
            logger.error_log_message(str(error.__traceback__))
            self.redis = None
            return



