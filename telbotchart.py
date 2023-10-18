import telebot


bot = telebot.TeleBot('6556831140:AAEwsGuiuywLcKpP21LMCujzJs5pqR9EzWk')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome ")


@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_message(message.chat.id, "Upmarket is a fintech startup that provides robo-advisory services to early-stage stock traders in India")


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Upmarket empowers traders with AI-driven insights and personalized strategies to enhance their stock market success.")

@bot.message_handler(func=lambda message: True)
def handle_other(message):
    bot.send_message(message.chat.id, "I don't understand this command. Type /help to see the available commands.")


bot.polling()
