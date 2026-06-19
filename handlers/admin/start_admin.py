from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.admin.admin import admin_keyboard, manage_products, back_to_products_panel_keyboard
from middlewares.admin_auth import AdminAuthentication
from database.models import Product, User, Order, Ticket
from database.config import SessionLocal

admin_router = Router()

admin_router.message.middleware(AdminAuthentication())

@admin_router.message(Command("admin"))
async def admin(message: Message):
    await message.reply("Panel Created ✅", reply_markup=admin_keyboard())
