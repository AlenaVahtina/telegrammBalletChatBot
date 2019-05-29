from telegram.ext import Updater, CommandHandler
import bot_config

def hi(bot, update):
    print('test')

def main():
    my_bot = Updater(bot_config.TOKEN, request_kwargs={
        'proxy_url' : bot_config.SOCKS_PROXY
    })

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', hi))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()