from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji
from data.locations import at_all, host_all, cafe_all

type_of_place = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Достопримечательности{emoji.emojize(':ferris_wheel:')}"),
        ],
        [
            KeyboardButton(text=f"Места поесть{emoji.emojize(':pizza:')}"),
        ],
        [
            KeyboardButton(text=f"Интересный факт{emoji.emojize(':pushpin:')}"),
        ],
        [
            KeyboardButton(text=f"Гостиницы{emoji.emojize(':house:')}"),
        ],
        [
            KeyboardButton(text=f"Погода{emoji.emojize(':sun:')}"),
        ],
    ], resize_keyboard=True,
)

atract_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
for place in at_all:
    atract_menu.insert(KeyboardButton(text=place["name"]))

hostel_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
for place in host_all:
    hostel_menu.insert(KeyboardButton(text=place["name"]))

cafe_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
for place in cafe_all:
    cafe_menu.insert(KeyboardButton(text=place["name"]))

