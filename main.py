from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import buttons
from config import TOKEN


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    await message.answer(f"{message.chat.first_name} Выберите нужный вам ресторан",reply_markup=buttons.replykb)
    print("Нажата кнопка старт")


@dp.message_handler(content_types="text")
async def process_start_command(message: types.Message):
    if message.text ==  "Ресторан1":
        await message.answer(f"{message.chat.first_name} Выберите нужный вам ресторан", reply_markup=buttons.button(message.chat.first_name))
    elif message.text == "Ресторан2":
        await message.answer(f"{message.chat.first_name} Выберите нужный вам ресторан",
                             reply_markup=buttons.button("точно это место?"))
    elif message.text == "Ресторан3":
        await message.answer(f"{message.chat.first_name} Выберите нужный вам ресторан",
                             reply_markup=buttons.button(message.chat.first_name))





if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)