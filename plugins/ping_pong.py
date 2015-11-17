"""
# Config (valid YAML document) must be at __doc__.
name: ping_pong # Name of plugin, lowercase, match with
                # file or package name.
description: "Example plugin for testing bot."
config:                            # Config variable that needed to set
  - SHELDON_PING_PONG_REPLY: '>>>' # in environment.
                                   # You can set default values after colon.
"""

import sheldon


@sheldon.hooks.message('hello, bot')
def ping_pong():
    pass
