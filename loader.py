from aiogram import Bot, Dispatcher, types
import config
import logging

from language_middlewares import setup_middleware

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

# Setup logging
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)
# Настроим i18n middleware для работы с многоязычностью
i18n = setup_middleware(dp)
# Создадим псевдоним для метода gettext
_ = i18n.gettext