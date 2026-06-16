from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.admin import admin_keyboard
from middlewares.admin_auth import AdminAuthentication

admin_router = Router()

admin_router.message.middleware(AdminAuthentication())

@admin_router.message(Command("admin"))
async def admin(message: Message):
    await message.reply("Panel Created ✅", reply_markup=admin_keyboard())
    
    
@admin_router.message(F.text == "Manage Database 📒")
async def db_management(message: Message):
    pass