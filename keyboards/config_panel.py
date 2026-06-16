from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.config import session_local
from database.models import Product


def config_panel_kb():
    config_main_kb = InlineKeyboardBuilder()
    
    config_main_kb.button(text="Show Plans 🚀", callback_data="show_plans")
    config_main_kb.button(text="Back To Main Menu 🔙", callback_data="back_to_menu")
    
    return config_main_kb.as_markup()

def plans_list():
    config_list_kb = InlineKeyboardBuilder()
    db = session_local()
    products = db.query(Product)
    
    for product in products:
        config_list_kb.button(text=product.subject, callback_data=f"plan_{product.id}_show")
    
    config_list_kb.adjust(2)
    
    db.close()
    return config_list_kb.as_markup()
        