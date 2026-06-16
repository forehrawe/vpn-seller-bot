from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton

def admin_keyboard():
    admin_main_keyboard = ReplyKeyboardBuilder()
    
    admin_main_keyboard.add(
        KeyboardButton(text="Manage Products 📦"),
        KeyboardButton(text="Manage Orders 🛒"),
        KeyboardButton(text="Manage Users 👥"),
        KeyboardButton(text="Manage Admins 👑"),
        KeyboardButton(text="Tickets 🎫"),
    )
    admin_main_keyboard.adjust(2)
    return admin_main_keyboard.as_markup(resize_keyboard=True)

def manage_products():
    manage_products_keyboard = InlineKeyboardBuilder()

    manage_products_keyboard.button(text="Show Products 📦", callback_data="show_products")
    manage_products_keyboard.button(text="New Product ➕", callback_data="new_product")
    manage_products_keyboard.button(text="Remove Product 🗑️", callback_data="remove_product")
    manage_products_keyboard.button(text="Edit Products ✏️", callback_data="edit_products")

    manage_products_keyboard.adjust(1)
    return manage_products_keyboard.as_markup()



def back_to_products_panel_keyboard():
    back_to_products = InlineKeyboardBuilder()

    back_to_products.button(text="Back 🔙", callback_data="back_to_products_panel")

    return back_to_products.as_markup()