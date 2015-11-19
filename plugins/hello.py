"""
# Config (valid YAML document) must be at __doc__.
name: hello     # Name of plugin, lowercase, match with
                # file or package name.
description: "Example plugin for testing bot."
config:                            # Config variable that needed to set
  - SHELDON_PING_PONG_REPLY: 'Hi' # in environment.
                                   # You can set default values after colon.
"""

import sheldon


@sheldon.hooks.message(['hello, bot', 'hey, bot'])
def hello_message(message, bot):
    answer = sheldon.OutgoingMessage(text='Hello, user', attachments=[])
    bot.send_message(answer)


@sheldon.hooks.command('hello')
def hello_command(message, bot):
    answer = sheldon.OutgoingMessage(text='Hello, user', attachments=[])
    bot.send_message(answer)
