from telegram.ext import CommandHandler
from funcs import login_func


def login_callback(update, context):
    uid = update.effective_message.from_user.id
    mid = context.bot.send_message(chat_id=uid,
                                   text='<code>OK!\nLogging you in...</code>',
                                   parse_mode='HTML').message_id

    login_func()

    context.bot.edit_message_text(chat_id=uid,
                                  message_id=mid,
                                  text='<code>DONE!\nJust logged you in!</code>',
                                  parse_mode='HTML')


login_handler = CommandHandler(command='login',
                               callback=login_callback)


def relogin_callback(update, context):
    uid = update.effective_message.from_user.id
    mid = context.bot.send_message(chat_id=uid,
                                   text='<code>OK!\nLogging you out...</code>',
                                   parse_mode='HTML').message_id

    login_func(action='Logout')

    context.bot.edit_message_text(chat_id=uid,
                                  message_id=mid,
                                  text='<code>DONE!\nJust logged you out!</code>',
                                  parse_mode='HTML')


relogin_handler = CommandHandler(command='relogin',
                                 callback=relogin_callback)

