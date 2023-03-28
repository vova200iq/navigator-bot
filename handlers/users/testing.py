from aiogram import types
from aiogram.dispatcher.filters import Command, CommandHelp, CommandStart, Text
from loader import dp
from states import Test
from aiogram.dispatcher import FSMContext


@dp.message_handler(Command("test"))
async def test_command(message: types.Message):
    await message.answer("Начинаем тестирование!")
    await message.answer("Итак, первый вопрос.\n\n"
                         "Какой квантум самый лучший?")

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    # await state.update data (
    #      {
    #            "answer1": answer
    #       }
    # )
    # async with state.proxy () as data:
    #      data["answer1"] = answer

    await message.answer("Второй вопрос\n\n"
                         "Кто лучший преподователь на свете?")
    await Test.Q2.set()
    # await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    await state.update_data(answer2=message.text)
    data = await state.get_data()
    ans1 = data["answer1"]
    ans2 = data["answer2"]
    await message.answer("Поздравляю! Вы прошли тест.\n\n"
                         "Ваши ответы:\n "
                         f"Первый ответ: <b>{ans1} </b>\n"

                         f"Второй ответ:<b>{ans1}</b>"

                         )

    await state.finish()


@dp.message_handler(CommandStart(), state="*")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ты нажал кнопку старт!\n"
                         "Набери /test и запуститься тестирование!")


@dp.message_handler(Command("cancel"), state="*")
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cancel_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ладно, закончим столь сложный тест")



