import logging
from decouple import config
from telegram.ext import Updater
from handlers import login_handler, relogin_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.getLevelName(config('LOG_LEVEL',
                                                      default='DEBUG')))


bot_token = config('BOT_TOKEN')
upd = Updater(bot_token,
              use_context=True)
dp = upd.dispatcher


def main():

    dp.add_handler(login_handler)
    dp.add_handler(relogin_handler)

    upd.start_polling()
    logging.info("Ready and listening for updates...")

    upd.idle()


if __name__ == '__main__':
    main()
