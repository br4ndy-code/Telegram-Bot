from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp

@dp.message_handler(Command('start'))
async def registration(message: Message):
    await message.answer(text='Welcome to our bot!')