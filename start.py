from sheldon import Sheldon

# Simulate command line arguments
# TODO
bot = Sheldon({'config-prefix': 'SHELDON_',
               'adapter': 'console'})
print(bot.start())
