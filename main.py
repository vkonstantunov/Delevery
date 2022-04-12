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
    await message.answer("Выберите нужный вам ресторан",reply_markup=buttons.replykb)
    print("Нажата кнопка старт")




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)