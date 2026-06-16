from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main_reply_markup_keyboard import main_kboard
from middlewares.user_registration import UserRegistration

start_router = Router()

start_router.message.middleware(UserRegistration())

@start_router.message(Command('start'))
async def start(message: Message, is_new_user: bool):
    if is_new_user:
        await message.answer('Welcome To Config Seller Bot 🗨', reply_markup=main_kboard())
    else:
        await message.answer('You Can Select an Option In Keyboard 🗨', reply_markup=main_kboard())
