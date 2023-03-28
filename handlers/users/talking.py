from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text, Command, CommandStart, CommandHelp
from loader import dp

@dp.message_handler(CommandStart())
async def process_start_command(message: types.Message):
    await message.answer('Давай начнём общение')

@dp.message_handler(Text(equals=['Привет', 'Ку', 'Салют'], ignore_case=True))
async def process_game_command(message: types.Message):
    await message.answer('Привет! Как дела?')


@dp.message_handler(Text(equals=['Нормально', 'Пойдёт', 'Ок'], ignore_case=True))
async def process_game_command(message: types.Message):
    await message.answer('У меня тоже неплохо...')





