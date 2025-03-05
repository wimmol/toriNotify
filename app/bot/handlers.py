import os

from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import Router
from dotenv import load_dotenv

from app.bot.keyboards import main_keyboard

load_dotenv()
ALLOWED_CHAT_ID = int(os.getenv("ALLOWED_CHAT_ID", "0"))

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    if message.chat.id != ALLOWED_CHAT_ID:
        return
    print(message.from_user.first_name)
    await message.answer(
        text=f'Привет, {message.from_user.first_name}',
        reply_markup=main_keyboard
    )

