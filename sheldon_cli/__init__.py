import os


def new():
    project_name = ''
    while not project_name:
        project_name = input('Enter name for project: ')
    os.makedirs(project_name + '/adapters')
    os.makedirs(project_name + '/data/log')
    os.mkdir(project_name + '/plugins')
    print('Created directories')

    start_file = open(project_name + '/start.py', 'w')
    start_file.write("""
import argparse
from sheldon import Sheldon

parser = argparse.ArgumentParser(description='Start bot')
parser.add_argument('--config-prefix', type=str, default='SHELDON_',
                    help='a str from which starting all config variables')
parser.add_argument('--adapter', type=str, default='console',
                    help='a str with name of adapter from adapters folder'
                         'or PyPi')
args = parser.parse_args()

bot = Sheldon({'config-prefix': args.config_prefix,
               'adapter': args.adapter})

bot.start()
    """)
    start_file.close()
    print('Created start.py')

    plugin_file = open(project_name + '/plugins/hello.py', 'w')
    plugin_file.write("""
\"\"\"
# Config (valid YAML document) must be at __doc__.
name: hello     # Name of plugin, lowercase, match with
                # file or package name.
description: "Example plugin for testing bot."
config:                          # Config variable that needed to set
  SHELDON_HELLO_REPLY: 'Hi'      # in environment.
                                 # You must set default values after colon.
\"\"\"

import sheldon
import sheldon.utils.logger
import schedule


@sheldon.hooks.message(['hello, bot', 'hey, bot'])
def hello_message(message, bot):
    answer = sheldon.OutgoingMessage(text=bot.config.get('SHELDON_HELLO_REPLY'),
                                     attachments=[])
    bot.send_message(answer)


@sheldon.hooks.command('hello')
def hello_command(message, bot):
    answer = sheldon.OutgoingMessage(text=bot.config.get('SHELDON_HELLO_REPLY'),
                                     attachments=[])
    bot.send_message(answer)


@sheldon.hooks.interval(schedule.every(5).minutes)
def hello_interval(bot):
    sheldon.utils.logger.info_message('Hello from hello module')


    """)
    plugin_file.close()
    print('Created plugin file')

    adapter_file = open(project_name + '/adapters/console.py', 'w')
    adapter_file.write("""
\"\"\"
# Config (valid YAML document) must be at __doc__.
name: console # Name of adapter, lowercase, match with
              # file or package name.
description: "Example adapter for testing bot."
config:                         # Config variable that needed to set
  SHELDON_CONSOLE_PROMPT: '>>>' # in environment.
                                # You can set default values after colon.
\"\"\"
from os import getlogin
from time import sleep
from random import randint
from sheldon.adapter import IncomingMessage, Attachment

# Code running on adapter loading may be here


def get_messages(bot):
    while True:
        # Let plugin thread end
        sleep(1)
        text = input('Enter message: ')

        attachments = []
        # For our example, attachment will be looking like:
        # '[type]_[path]'
        received_attachments = input(
            'Enter a comma-separated attachments'
            '(<type>_<path>):'
        ).split(',')

        # If user don't enter attachment,
        # message_attachments will be empty
        if received_attachments[0]:
            for attachment in received_attachments:
                # Parse incoming attachment:
                # attachment_data[0] will be attachment type
                # attachment_data[1] will be attachment path
                attachment_data = attachment.split('_')
                if len(attachment_data) < 2:
                    print('Incorrect attachment "{}"'.format(attachment))
                    continue
                attachments.append(Attachment(
                    attachment_type=attachment_data[0],
                    attachment_path=attachment_data[1:],
                    attachment_id=randint(1, 1000000000)  # Fake id
                ))

        yield IncomingMessage(sender=User(username=getlogin()), text=text,
                              attachments=attachments, variables={
                                  # Fake message id
                                  'console_id': randint(1, 1000000000)
                              })


def send_message(message, bot):
    print('BOT: ', message.text)
    print('Channel: ', message.channel)
    print('Attachments:')
    for attachment in message.attachments:
        print(attachment.id)
        print(attachment.type)
        print(attachment.path)
        print(attachment.text)


# Adapter must have implementation of User class.
class User:
    def __init__(self, username):
        \"\"\"
        Create new User for console adapter

        :param username: name in bash session
        :return:
        \"\"\"
        # Adapter object should have 'id' and 'username' params.
        self.id = hash(username)
        self.username = username


    """)
    adapter_file.close()
    print('Created adapter file')

    plugins_file = open(project_name + '/installed_plugins.txt', 'w')
    plugins_file.write("""plugins.hello\n""")
    plugins_file.close()
    print('Created installed plugins file')

    print('Project created')




