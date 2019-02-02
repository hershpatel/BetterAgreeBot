import telebot

token = "553019456:AAHvfO3eeYeSLtZv8s75_z8rmVLtaaInqXw"

bot = telebot.TeleBot(token = token)

@bot.message_handler(commands = ['start'])
def HelloWorld(message):
    bot.reply_to(message, "Hello World!")

@bot.message_handler(content_types = ['text'])
def echo_all(message):
    print(message.from_user)
    bot.send_message(message.from_user.id, message.text)

bot.polling()
