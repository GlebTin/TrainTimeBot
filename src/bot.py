import telebot
from telebot import types


bot = telebot.TeleBot('7064548980:AAEJa6IwjBbooyf0UBMyOwJS0ieTLzjnwlk')


name = ''
surname = ''
age = ''


@bot.message_handler(func=lambda message:True)
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
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    try:
        age = int(message.text)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)
        question = f'''You`re {str(age)}years old and your name is {name} {surname}?'''
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.from_user.id, 'Please enter the value in digits.')

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == 'yes':
            bot.send_message(message.from_user.id, 'I got it!')
        elif call.data == 'no':
            bot.send_message(message.from_user.id, 'Please repeat, write /reg')


bot.polling(none_stop=True, interval=0)
