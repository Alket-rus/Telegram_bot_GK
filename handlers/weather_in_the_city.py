from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.weather_city_keyboards import make_row_keyboard
from handlers.city.weather_search_mo import city_choice_MO_weather
from handlers.city.weather_search_lo import city_choice_LO_weather
from handlers.city.weather_search_ko import city_choice_KO_weather

router_weather = Router()

awailable_area_names = ['Московская область', 'Ленинградская область', 'Калужская область']
awailable_city_MO_names = ['Москва', 'Мытищи', 'Химки']
awailable_city_LO_names = ['Санкт-Петербург', 'Всеволожск', 'Выборг']
awailable_city_KO_names = ['Калуга', 'Обнинск', 'Малоярославец']

class Weather_Area_Name(StatesGroup):
    choice_area_names = State()
    choice_city_MO_names = State()
    choice_city_MO_weather = State()
    choice_city_LO_names = State()
    choice_city_LO_weather = State()
    choice_city_KO_names = State()
    choice_city_KO_weather = State()


@router_weather.message(Command('area'))
@router_weather.message(F.text.lower() == 'погода')
@router_weather.message(Command('p'))
async def cmd_area(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя видеть {name}! Выбери свою область", reply_markup=make_row_keyboard(awailable_area_names))
    await state.set_state(Weather_Area_Name.choice_area_names)

@router_weather.message(Weather_Area_Name.choice_area_names,  F.text.in_(awailable_area_names[0]))
async def city_choice_MO(message: types.Message, state: FSMContext):
        await state.update_data(choice_city_MO_names=message.text.lower())
        await message.answer(f"Выбери свой 🌇город", reply_markup=make_row_keyboard(awailable_city_MO_names))
        await state.set_state(Weather_Area_Name.choice_city_MO_names)

@router_weather.message(Weather_Area_Name.choice_area_names,  F.text.in_(awailable_area_names[1]))
async def city_choice_MO(message: types.Message, state: FSMContext):
        await state.update_data(choice_city_LO_names=message.text.lower())
        await message.answer(f"Выбери свой 🌃город", reply_markup=make_row_keyboard(awailable_city_LO_names))
        await state.set_state(Weather_Area_Name.choice_city_LO_names)

@router_weather.message(Weather_Area_Name.choice_area_names,  F.text.in_(awailable_area_names[2]))
async def city_choice_MO(message: types.Message, state: FSMContext):
        await state.update_data(choice_city_KO_names=message.text.lower())
        await message.answer(f"Выбери свой 🏙️город", reply_markup=make_row_keyboard(awailable_city_KO_names))
        await state.set_state(Weather_Area_Name.choice_city_KO_names)

@router_weather.message(Weather_Area_Name.choice_area_names)
async def city_choice_incorrectly(message: types.Message):
        await message.answer(text='Не знаю такой области', reply_markup=make_row_keyboard(awailable_area_names))


@router_weather.message(Weather_Area_Name.choice_city_MO_names,  F.text.in_(awailable_city_MO_names))
async def city_choice_MO(message: types.Message, state: FSMContext):
        user_city = message.text.lower()
        await message.answer(f"{city_choice_MO_weather(user_city)}", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Weather_Area_Name.choice_city_MO_weather)

@router_weather.message(Weather_Area_Name.choice_city_LO_names,  F.text.in_(awailable_city_LO_names))
async def city_choice_LO(message: types.Message, state: FSMContext):
        user_city = message.text.lower()
        await message.answer(f"{city_choice_LO_weather(user_city)}", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Weather_Area_Name.choice_city_KO_weather)

@router_weather.message(Weather_Area_Name.choice_city_KO_names,  F.text.in_(awailable_city_KO_names))
async def city_choice_KO(message: types.Message, state: FSMContext):
        user_city = message.text.lower()
        await message.answer(f"{city_choice_KO_weather(user_city)}", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Weather_Area_Name.choice_city_KO_weather)

@router_weather.message(Weather_Area_Name.choice_city_MO_names)
@router_weather.message(Weather_Area_Name.choice_city_LO_names)
@router_weather.message(Weather_Area_Name.choice_city_KO_names)
async def city_choice_incorrectly(message: types.Message):
        await message.answer(text='Не знаю такого города', reply_markup=make_row_keyboard(awailable_city_MO_names))