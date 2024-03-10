from aiogram import types


button1 = types.KeyboardButton(text='Начать')
button2 = types.KeyboardButton(text='Информация')
button3 = types.KeyboardButton(text='Напиши какую нибудь цитату')
button4 = types.KeyboardButton(text='Расскажи анекдот')
button5 = types.KeyboardButton(text='Расскажи стих')
button6 = types.KeyboardButton(text='Погода')

keyboard1 = [
[button1, button2, button3],
[button4, button5, button6],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)