from sheldon import Sheldon

# Simulate command line arguments
bot = Sheldon({'config-prefix': 'SHELDON_',
               'adapter': 'console'})
print(bot.start())
