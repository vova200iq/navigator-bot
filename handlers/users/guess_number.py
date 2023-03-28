from aiogram import types
from random import randint
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text, Command
from loader import dp

user = {
    "in_game": False,
    "attempts": 5,
    "number": 0,
}


# @dp.message_handler(commands=['start'])
@dp.message_handler(CommandStart())
async def process_start_command(message: types.Message):
    await message.answer(
        'Привет!\nМеня зовут Эхо!\nДавай сыграем в игру "Угадай число"?\nЧтобы прочитать правила, используй команду '
        '/help')


# @dp.message_handler(commands=['help'])
@dp.message_handler(CommandHelp())
async def process_help_command(message: types.Message):
    await message.answer(
        '1. Я загадаю число от 1 до 100, а ты будешь должен его отгадать.\n'
        '2. Введи число. Если твоё предположение неверно, то я скажу, больше или меньше загаданное число, '
        'а затем предложу тебе повторить попытку.\n'
        '3. Если ты угадаешь, игра завершится.\n'
        '4. Количество попыток ограничено. :)\n'
        '5. Ты можешь завершить игру с помощью команды /cancel')


@dp.message_handler(Command("cancel"))
async def cancel(message: types.Message):
    if user["in_game"]:
        await message.answer("Ну ладно.\n"
                             "Сыграем в другой раз?")
        user["in_game"] = False
    else:
        await message.answer("Ты и так не в игре!")


@dp.message_handler(Text(equals=['Да', 'Давай', 'Сыграем'], ignore_case=True))
async def send_agree_answer(message: types.Message):
    # bot.send_message(chat_id=,text=)
    await message.answer("Очень рад поиграть!\n"
                         "Я загадал, попробуй угадай.")
    user["number"] = randint(1, 100)
    user["in_game"] = True
    user["attempts"] = 5


@dp.message_handler(Text(equals=['Нет', 'Не хочу', 'В другой раз'], ignore_case=True))
async def send_disagree_answer(message: types.Message):
        await message.answer("Как хочешь.")


@dp.message_handler(Text(equals=[str(i) for i in range(1, 101)]))
async def send_some_number(message: types.Message):
    if user["in_game"]:
        if int(message.text) == user["number"]:
            await message.answer("Ты угадал!")
            user["in_game"] = False
            user["attempts"] = 5
            user["number"] = 0
        elif int(message.text) > user["number"]:
            user["attempts"] -= 1
            await message.answer(f'Ты не угадал! Загаданное число меньше. Осталось попыток: {user["attempts"]}')
        elif int(message.text) < user["number"]:
            user["attempts"] -= 1
            await message.answer(f'Ты не угадал! Загаданное число больше. Осталось попыток: {user["attempts"]}')
        if user["attempts"] == 0:
            await message.answer(f"Ты проиграл. Я загадал число {user['number']}.")
            user["in_game"] = False
        print(user['number'])


@dp.message_handler()
async def send_some_other(message: types.Message):
        if user["in_game"]:
            await message.answer(f"Я тебя не понимаю. '{message.text}' - не число!")
        else:
            await message.answer("Я тебя не понял. Хочешь сыграть?")

