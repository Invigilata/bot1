from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7344198166:AAGSLiBsQ4yRiUJuvAzNqJXV_zJufXK0l-I'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Асинхронная функция, запускаемая по команде '/start'
@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

# Асинхронная функция, запускаемая при любом другом сообщении
@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
