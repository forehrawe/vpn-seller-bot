from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.admin import admin_keyboard, manage_products, back_to_products_panel_keyboard
from middlewares.admin_auth import AdminAuthentication
from database.models import Product, User, Order, Ticket
from database.config import session_local

admin_router = Router()

admin_router.message.middleware(AdminAuthentication())

@admin_router.message(Command("admin"))
async def admin(message: Message):
    await message.reply("Panel Created ✅", reply_markup=admin_keyboard())
    
    
@admin_router.message(F.text == "Manage Products 📦")
async def db_management(message: Message):
    await message.answer("Products Panel 📦", reply_markup=manage_products())



# callback_query
@admin_router.callback_query(F.data == "show_products")
async def show_products(callback: CallbackQuery):
    db = session_local()
    products = db.query(Product).all()
    products_text = "\n".join(
    [
        f"📦 Subject: {p.subject}\n"
        f"🌍 Region: {p.region}\n"
        f"📏 Volume: {p.volume}GB\n"
        f"💰 Price: {p.price} Toman\n"
        for p in products
    ]
)

    await callback.message.edit_text(products_text, reply_markup=back_to_products_panel_keyboard())

@admin_router.callback_query(F.data == "back_to_products_panel")
async def back_to_products_panel(callback: CallbackQuery):
    await callback.message.edit_text("Products Panel 📦", reply_markup=manage_products())