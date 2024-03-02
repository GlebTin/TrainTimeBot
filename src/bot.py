import telebot

bot = telebot.TeleBot('7064548980:AAEJa6IwjBbooyf0UBMyOwJS0ieTLzjnwlk')


name = ''
surname = ''
age = ''

@bot.message_handler(func=lambda message: True) #content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Hello!\n"
                                               "What`s you name?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Write /reg")


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "What`s you surname?")
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "How old are you?")
    bot.register_message_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Please enter the value in digits.')
    bot.send_message(message.from_user.id, 'Your age is ' + str(age) + ', your name is '
                         + name + surname + '?')


bot.polling(none_stop=True, interval=0)