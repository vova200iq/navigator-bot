from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import emoji
loc_keyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Найти меня {emoji.emojize(':mag:')} " )
        ]
    ], resize_keyboard=True
)