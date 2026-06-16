from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def admin_keyboard():
    admin_main_keyboard = ReplyKeyboardBuilder()
    
    admin_main_keyboard.add(
        KeyboardButton("Manage Database 📒"),
        KeyboardButton("Tickets 🎫")
    )
    admin_main_keyboard.adjust(2)
    return admin_main_keyboard.as_markup(resize_keyboard=True)