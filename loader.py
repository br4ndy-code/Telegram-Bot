from aiogram import Bot, Dispatcher, types
import config
import logging

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

# Setup logging
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)