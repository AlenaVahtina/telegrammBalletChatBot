from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bot_config
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def hi(update, context):
    update.message.reply_text('Привет. С помощью команд ты можешь узнать расписание, стоимость,'
                'адрес или время проведения занятий. Если у тебя есть другие вопросы, можешь написать и в '
                'скором времени кто-нибудь и администраторов тебе обязательно ответит! \n'
                '/date - расписание \n'
                '/adress - адрес \n'
                '/price - стоимость')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    my_bot = Updater(bot_config.TOKEN, request_kwargs=bot_config.REQUEST_KWARGS)

    dp = my_bot.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", hi))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    my_bot.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    my_bot.idle()


if __name__ == '__main__':
    main()