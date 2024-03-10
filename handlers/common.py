from aiogram import types, F, Router
from aiogram.filters.command import Command
from keyboards.keyboards import kb1
from utils.joke import joke
from utils.quote import quote
from utils.poem import poem
from keyboards.keywords import keywords_joke, keywords_quote, keywords_cmd_info, keywords_poem, keywords_hello

router_common = Router()

@router_common.message(Command('start'))
@router_common.message(F.text.lower() == 'начать')
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя выдеть {name}!", reply_markup=kb1)

async def keyboards_print(message: types.Message):
    await message.answer(text="Выберите действие:", reply_markup=kb1)

@router_common.message(Command('info'))
@router_common.message(F.text.lower() == 'информация')
async def cmd_info(message: types.Message):
    print(message.chat)
    await message.answer("Я веселый телеграмм бот!")
    await message.answer("Основные команды:")
    await message.answer("/start")
    await message.answer("/info")
    await message.answer("/joke")
    await message.answer("/quote")
    await message.answer("/poem")

@router_common.message(Command('joke'))
@router_common.message(Command('анекдот'))
@router_common.message(F.text.lower() == 'расскажи анекдот')
async def joke_print(message: types.Message):
    await message.answer("Анекдот!")
    text_jokes = joke()
    await message.answer(text_jokes, reply_markup=kb1)

@router_common.message(Command('quote'))
@router_common.message(Command('цитата'))
@router_common.message(F.text.lower() == 'напиши какую нибудь цитату')
async def quote_print(message: types.Message):
    await message.answer("Цитата!")
    text_quote = quote()
    await message.answer(text_quote, reply_markup=kb1)

@router_common.message(Command('poem'))
@router_common.message(Command('стих'))
@router_common.message(F.text.lower() == 'расскажи стих')
async def poem_print(message: types.Message):
    await message.answer("Стих!")
    text_poem = poem()
    await message.answer(text_poem, reply_markup=kb1)

@router_common.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    if  any(keyword in msg_user for keyword in keywords_joke):
        await joke_print(message)
    elif any(keyword in msg_user for keyword in keywords_quote):
        await quote_print(message)
    elif any(keyword in msg_user for keyword in keywords_cmd_info):
        await cmd_info(message)
    elif any(keyword in msg_user for keyword in keywords_poem):
        await poem_print(message)
    elif any(keyword in msg_user for keyword in keywords_hello):
        await message.answer('Привет!', reply_markup=kb1)
    else:
        await message.answer('Я не знаю такого слова!', reply_markup=kb1)
