import telebot
from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
eng_ru = {
    "q": "й",
    "w": "ц",
    "e": "у",
    "r": "к",
    "t": "е",
    "y": "н",
    "u": "г",
    "i": "ш",
    "o": "щ",
    "p": "з",
    "[": "х",
    "]": "ъ",
    "a": "ф",
    "s": "ы",
    "d": "в",
    "f": "а",
    "g": "п",
    "h": "р",
    "j": "о",
    "k": "л",
    "l": "д",
    ";": "ж",
    "'": "э",
    "z": "я",
    "x": "ч",
    "c": "с",
    "v": "м",
    "b": "и",
    "n": "т",
    "m": "ь",
    ",": "б",
    ".": "ю",
    "`": "ё",
    # caps
    "~": "ё",
    "{": "х",
    "}": "ъ",
    "<": "б",
    ">": "ю"}


def func(msg):
    new_text = ""
    for i in msg:
        if i in eng_ru:
            new_text += eng_ru[i]
        else:
            new_text += i
    return new_text


# @bot.message_handler(commands=['work'])
@bot.message_handler(content_types=["text"])
def translate(message):
    bot.reply_to(message, func(message.text))


bot.polling()