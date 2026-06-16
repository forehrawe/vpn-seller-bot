from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def main_kboard():
    main_keyboard = ReplyKeyboardBuilder()
    main_keyboard.add(
        KeyboardButton(text="Config Panel ▶"),
        KeyboardButton(text="Support 💭"),
        KeyboardButton(text="Increase Wallet 💲"),
        KeyboardButton(text="-------"),
        KeyboardButton(text="-------")
    )
    main_keyboard.adjust(2)
    return main_keyboard.as_markup(resize_keyboard=True)