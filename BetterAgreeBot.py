import telebot
from telebot import types

token = "553019456:AAHvfO3eeYeSLtZv8s75_z8rmVLtaaInqXw"

bot = telebot.TeleBot(token = token)


def new_poll_keyboard(chat_id):
    new_poll_keyboard = types.ReplyKeyboardMarkup(row_width = 1)
    new_poll_button = types.KeyboardButton('/newpoll')
    new_poll_keyboard.add(new_poll_button)
    bot.send_message(chat_id,"Thanks for choosing BetterAgreeBot", reply_markup = new_poll_keyboard)

def remove_markup_keyboard(chat_id):
    remove = types.ReplyKeyboardRemove()
    bot.send_message(chat_id,"",reply_markup = remove)


@bot.message_handler(commands = ['start'])
def HelloWorld(message):
    bot.reply_to(message, "Hello World!")
    new_poll_keyboard(message.from_user.id)

@bot.message_handler(commands = ['newpoll'])
def new_poll(message):
    remove_markup_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,"Your new poll has been created!", reply_markup = remove_markup_keyboard)
    force_reply = types.ForceReply()
    bot.send_message(message.from_user.id,"Please REPLY with your Question.", reply_markup=force_reply)
    x = bot.get_updates()
    for message in x:
        print message.reply_to_message.text

@bot.message_handler(content_types = ['text'])
def echo_all(message):
    print(message.from_user)
    bot.send_message(message.from_user.id, message.text)

bot.polling()
