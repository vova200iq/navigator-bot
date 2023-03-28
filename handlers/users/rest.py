from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import random
from keyboards.default.menu_keyboard import atract_menu, hostel_menu, cafe_menu
from loader import dp
from aiogram.dispatcher.filters import Command, Text, CommandStart
from aiogram import types
from keyboards.default import type_of_place
from states import ChoseType
from data.locations import at_all, host_all, cafe_all
from data.locations import interesting_facts, fact_indexes

@dp.message_handler(Command("start"), state="*")
async def show_menu(message: types.Message, state: FSMContext):
    await message.answer("Приветствую! Куда желаете направиться?", reply_markup=type_of_place)
    await state.finish()


@dp.message_handler(Text(contains=f"Достопримечательности"))
@dp.message_handler(Command("attractions"))
async def get_dostup(message: types.Message):
    await message.answer("Выберите одну из достопримечательностей", reply_markup=atract_menu)
    await ChoseType.At.set()


@dp.message_handler(Text(contains="Гостиницы"))
@dp.message_handler(Command("hostel"))
async def get_hostel(message: types.Message):
    await ChoseType.Hotel.set()
    await message.answer("Выберете гостиницу:", reply_markup=hostel_menu)

@dp.message_handler(Text(contains="Места поесть"))
@dp.message_handler(Command("cafe"))
async def get_hostel(message: types.Message):
    await ChoseType.Cafe.set()
    await message.answer("Выберете кафе:", reply_markup=cafe_menu)

@dp.message_handler(Text(contains="Погода"))
@dp.message_handler(Command("weather"))
async def get_weather(message: types.Message):
    text = "<a href='https://yandex.ru/pogoda/magadan?lat=59.549537&lon=150.804077'>Погода в Магадане</a>"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(contains=f"Интересный факт"),state="8")
@dp.message_handler(Command("fact"),state="*")
async def get_dostup(message: types.Message):
    while True:
        fact = random.choice(interesting_facts)
        if interesting_facts.index(fact) not in fact_indexes:
            fact_indexes.append(interesting_facts.index(fact))
            await message.answer(fact)
            break
        if len(interesting_facts) == len(fact_indexes):
            await message.answer("Факты закончились")
            fact_indexes.clear()


@dp.message_handler(state=ChoseType.Cafe)
async def catch_cafe(message: types.Message, state: FSMContext):
    await state.finish()
    await get_cafe(message)


async def get_cafe(message):
    for elem in cafe_all:
        if elem["name"] == message.text:
            await message.answer_photo(elem["photo"], caption=elem["desc"], reply_markup=ReplyKeyboardRemove())
            await message.answer_location(latitude=elem["coord"]["lat"],
                                          longitude=elem["coord"]["lon"])
            break


@dp.message_handler(state=ChoseType.At)
async def catch_atract(message: types.Message, state: FSMContext):
    await state.finish()
    await get_atract(message)


@dp.message_handler(state=ChoseType.Hotel)
async def cath_hostel(message: types.Message, state: FSMContext):
    await state.finish()
    await get_hostel(message)


async def get_atract(message: types.Message):
    for elem in at_all:
        if elem["name"] == message.text:
            await message.answer_photo(elem["photo"], caption=elem["desc"], reply_markup=ReplyKeyboardRemove())
            await message.answer_location(latitude=elem["coord"]["lat"],
                                          longitude=elem["coord"]["lon"])
            break


async def get_hostel(message: types.Message):
    for elem in host_all:
        if elem["name"] == message.text:
            await message.answer_photo(photo=elem["photo"], caption=elem["desc"], reply_markup=ReplyKeyboardRemove())
            await message.answer_location(latitude=elem["coord"]["lat"],
                                          longitude=elem["coord"]["lon"])
# print(message.text)
# location = message.location
# lat = location.latitude
# lon = location.longitude
# closest_place = choose_shortesrt(location, Attract)
# text_format = "Название {place_name}\n" \
#               "Расстояние до него: {distance: .1f} км."
# text = "\n\n".join(
#     [
#         text_format.format(place_name=place_name, distance=distance)
#         for place_name, distance, url, place_location in closest_place
#     ]
# )
#
# ind = random.randint(0, len(at) - 1)
# await message.answer("Вы выбрали достопримечательность:", reply_markup=ReplyKeyboardRemove())
# await message.answer_photo(at[ind], caption=desc[ind])

# @dp.message_handler(content_types=types.ContentType.LOCATION, state=)

# @dp.message_handler(Text(contains=f"Места поесть"))
# @dp.message_handler(Command("cafe"))
# async def get_eating(message: types.Message):
#     await message.answer("Вы выбрали места для поесть:", reply_markup=ReplyKeyboardRemove())

# @dp.message_handler(Text(contains=f"Интересный факт"))
# @dp.message_handler(Command("fact"))
# async def get_fact(message: types.Message):
#     await message.answer("Вы выбрали интересный факт:", reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message_handler(Text(contains=f"Гостинницы"))
# @dp.message_handler(Command("hostel"))
# async def get_host(message: types.Message):
#     ind = random.randint(0, len(host) - 1)
#     await message.answer("Вы выбрали гостинницы:", reply_markup=ReplyKeyboardRemove())
#     await message.answer_photo(host[ind], caption=infhost[ind])
#
#
# @dp.message_handler(Text(contains=f"Погода в Магадане"))
# @dp.message_handler(Command("weather"))
# async def get_weather(message: types.Message):
#     await message.answer("Вы выбрали погода:", reply_markup=ReplyKeyboardRemove())
