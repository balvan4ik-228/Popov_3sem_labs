import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8554739497:AAFkx3IiGKF9N4pavPlfNRntvxVmDBN3vgw"

class Form(StatesGroup):
    START = State()
    WAITING_NAME = State()
    WAITING_AGE = State()

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Form.START)
    await message.answer("Привет! Введи /name, чтобы начать.")

@dp.message(Command("name"), Form.START)
async def process_name_request(message: Message, state: FSMContext):
    await state.set_state(Form.WAITING_NAME)
    await message.answer("Введи свое имя:")

@dp.message(Form.WAITING_NAME)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.WAITING_AGE)
    await message.answer("Теперь введи свой возраст:")

@dp.message(Form.WAITING_AGE)
async def process_age(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    age = message.text
    await state.clear()  # Сброс состояния
    await message.answer(f"Привет, {name}! Тебе {age} лет. Диалог завершен. /start для нового.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
