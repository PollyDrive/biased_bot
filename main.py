import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode
import os
import json
import random


# JSON с искажениями
with open('biases.json', 'r', encoding='utf-8') as file:
    biases = json.load(file)


TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Напиши /get, чтобы получить случайное когнитивное искажение.")

@dp.message(Command('get'))
async def cmd_bias(message: Message):
    bias = random.choice(biases)
    text = f"*{bias['name']}*\n\n{bias['description']}"
    await message.answer(text)


# async def main():
#     await dp.start_polling(bot)

# if __name__== '__main__':
#     asyncio.run(main())

if __name__ == "__main__":
    try:
        asyncio.run(dp.start_polling(bot))
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")