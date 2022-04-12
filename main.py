from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import buttons
from func import *
from config import TOKEN


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    await message.answer(f"{message.chat.first_name} Выберите нужный вам ресторан",reply_markup=buttons.replykb1)
    print("Нажата кнопка старт")


@dp.message_handler(content_types="text")
async def process_start_command(message: types.Message):
    if message.text ==  "Ресторан1":
        await message.answer_photo(image("photo/logo/1629125620_content_700x455.jpg"),
                                   f"{message.chat.first_name} Вы выбрали {message.text}",
                             reply_markup=buttons.replykb)
    elif message.text == "Ресторан2":
        await message.answer_photo(image("photo/logo/1629125620_content_700x455.jpg"),
                             f"{message.chat.first_name} Вы выбрали {message.text}",
                             reply_markup=buttons.replykb)
    elif message.text == "Ресторан3":
        await message.answer_photo(image("photo/logo/1629125620_content_700x455.jpg"),
                             f"{message.chat.first_name} Вы выбрали {message.text}",
                             reply_markup=buttons.replykb)


@dp.message_handler(content_types="text")
async def pr(message: types.Message):
    if message.text == "Оформить заказ":
        await message.answer("Ведите свои данные", reply_markup=buttons.replykb1)





if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)