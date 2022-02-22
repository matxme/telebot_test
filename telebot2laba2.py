import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types

bot = telebot.TeleBot('5263931934:AAHVWoGfYzJCUgMZn3aC668VDxltezVND-U')  # Создаем экземпляр бота

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Main menu")
    btn2 = types.KeyboardButton("Help")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="ssup, {0.first_name}! этот бот написан для теста лаб-кода".format(
                         message.from_user), reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Main menu" or ms_text == "Main menu" or ms_text == "Back to main menu":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("some gags")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "some gags":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Back to main menu")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="some gags", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":  # .........................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Прислать анекдот":  # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Help" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Старинцев Роман")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/matxme")
        key1.add(btn1)
        #img = open('Швец Андрей.png', 'rb')
        #bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="несуществующая команда - Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()