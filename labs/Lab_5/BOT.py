import telebot
from telebot import types
from random import choice

TOKEN = '7002895044:AAEy5xl1MVl7-U23bareobY87vMP376Qbdc'
bot = telebot.TeleBot(TOKEN)

CARD_NUMBER = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_SUIT = ["♦", "♠", "♥", "♣"]


def generate_random_card():
    random_card_number = choice(CARD_NUMBER)
    random_card_suit = choice(CARD_SUIT)
    return random_card_suit, random_card_number


def get_card_color(suit):
    if suit in ["♦", "♥"]:
        return "красный"
    else:
        return "черный"


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    level_1 = telebot.types.KeyboardButton('1')
    level_2 = telebot.types.KeyboardButton('2')
    level_3 = telebot.types.KeyboardButton('3')
    level_4 = telebot.types.KeyboardButton('4')
    keyboard.row(level_1, level_2)
    keyboard.row(level_3, level_4)
    bot.send_message(message.chat.id,
                     "Выбери уровень сложности",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ['1', '2', '3', '4'])
def levels(message):
    if message.text == '1':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        red_button = telebot.types.KeyboardButton('🟥')
        black_button = telebot.types.KeyboardButton('⬛')
        back_button = telebot.types.KeyboardButton('Уровни')
        keyboard.row(red_button, black_button)
        keyboard.row(back_button)
        bot.send_message(message.chat.id, 'Выбери цвет карты', reply_markup=keyboard)

    elif message.text == '2':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        diamonds = telebot.types.KeyboardButton('♦')
        spades = telebot.types.KeyboardButton('♠')
        crosses = telebot.types.KeyboardButton('♣')
        hearts = telebot.types.KeyboardButton('♥')
        back_button = telebot.types.KeyboardButton('Уровни')
        keyboard.row(spades, hearts)
        keyboard.row(diamonds, crosses)
        keyboard.row(back_button)
        bot.send_message(message.chat.id, 'Выбери масть карты', reply_markup=keyboard)

    elif message.text == '3':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        number_2 = telebot.types.KeyboardButton('2')
        number_3 = telebot.types.KeyboardButton('3')
        number_4 = telebot.types.KeyboardButton('4')
        number_5 = telebot.types.KeyboardButton('5')
        number_6 = telebot.types.KeyboardButton('6')
        number_7 = telebot.types.KeyboardButton('7')
        number_8 = telebot.types.KeyboardButton('8')
        number_9 = telebot.types.KeyboardButton('9')
        number_10 = telebot.types.KeyboardButton('10')
        number_J = telebot.types.KeyboardButton('J')
        number_Q = telebot.types.KeyboardButton('Q')
        number_K = telebot.types.KeyboardButton('K')
        number_A = telebot.types.KeyboardButton('A')
        back_level = telebot.types.KeyboardButton('Уровни')
        keyboard.row(number_2, number_3, number_4, number_5, number_6, number_7)
        keyboard.row(number_8, number_9, number_10, number_J, number_Q, number_K)
        keyboard.add(number_A)
        keyboard.add(back_level)
        bot.send_message(message.chat.id, 'Выбери значение карты', reply_markup=keyboard)

    elif message.text == '4':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_button = telebot.types.KeyboardButton('Уровни')
        keyboard.add(back_button)
        bot.send_message(message.chat.id, 'Введите значение и масть карты\n(Пример: 10 ♥ или A ♦)',
                         reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ['🟥', '⬛', '♦', '♠', '♣', '♥', 'Уровни'])
def game_choices(message):
    if message.text == 'Уровни':
        start(message)
        return

    card_suit, card_number = generate_random_card()

    if message.text == '🟥':
        user_choice = "красный"
        correct_color = get_card_color(card_suit)
        if user_choice == correct_color:
            result = f"✅ Правильно! Карта: {card_number}{card_suit}\nЦвет: {correct_color}"
        else:
            result = f"❌ Неправильно! Карта: {card_number}{card_suit}\nЦвет: {correct_color}"
        bot.send_message(message.chat.id, result)

    elif message.text == '⬛':
        user_choice = "черный"
        correct_color = get_card_color(card_suit)
        if user_choice == correct_color:
            result = f"✅ Правильно! Карта: {card_number}{card_suit}\nЦвет: {correct_color}"
        else:
            result = f"❌ Неправильно! Карта: {card_number}{card_suit}\nЦвет: {correct_color}"
        bot.send_message(message.chat.id, result)

    elif message.text in ['♦', '♠', '♣', '♥']:
        if message.text == card_suit:
            result = f"✅ Правильно! Карта: {card_number}{card_suit}"
        else:
            result = f"❌ Неправильно! Карта: {card_number}{card_suit}"
        bot.send_message(message.chat.id, result)


@bot.message_handler(
    func=lambda message: message.text in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
def game_3(message):
    card_suit, card_number = generate_random_card()

    if message.text == card_number:
        result = f"✅ Правильно! Карта: {card_number}{card_suit}"
    else:
        result = f"❌ Неправильно! Карта: {card_number}{card_suit}"
    bot.send_message(message.chat.id, result)


@bot.message_handler(func=lambda message: True)
def game_4(message):
    if message.text == 'Уровни':
        start(message)
        return

    user_input = message.text.strip()
    card_suit, card_number = generate_random_card()

    try:
        parts = user_input.split()
        if len(parts) == 1:
            user_value = parts[0][:-1]
            user_suit = parts[0][-1]
        else:
            user_value = parts[0]
            user_suit = parts[1]

        user_value = user_value.upper()

        if user_suit == card_suit and user_value == card_number:
            result = f"✅ Правильно! Карта: {card_number}{card_suit}"
        else:
            result = f"❌ Неправильно! Карта: {card_number}{card_suit}"
        bot.send_message(message.chat.id, result)

    except:
        bot.send_message(message.chat.id, f"Неверный формат! Попробуйте снова. Карта была: {card_number}{card_suit}")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)