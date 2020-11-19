import telebot

bot = telebot.TeleBot('1323366674:AAGN4kApD2yEzx2juFABbMf7jJ8dcvyt-Qo')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привіт', 'На все добре')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, ти написав мені /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Привіт':
        bot.send_message(message.chat.id, 'Привіт, Тенор')
    elif message.text.lower() == 'Прощавай':
        bot.send_message(message.chat.id, 'Прощавай, Тенор')
    elif message.text.lower() == 'Слава Україні':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJX11-wXgSkoyhF_9CI6HooR9qemZL5AAKSAAN8BQcbxy1uiXl96QgeBA')
    elif message.text.lower() == 'дайте зарплату':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJX2l-wXlnlsr2wnnE3dMWwcFPoOZ7qAAJkAgACebI-BEe09NG8VscUHgQ')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()