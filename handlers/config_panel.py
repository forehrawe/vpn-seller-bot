from aiogram import Router
from aiogram.types import Message
from aiogram import F
from aiogram.types import CallbackQuery
from keyboards.config_panel import config_panel_kb, plans_list

config_panel_router = Router()

@config_panel_router.message(F.text == "Config Panel ▶")
async def config_panel(message: Message):
    await message.answer('Select a Pannel To Continue ✔', reply_markup=config_panel_kb())


@config_panel_router.callback_query(F.data == "show_plans")
async def show_plans(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=plans_list())
    
    
@config_panel_router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=config_panel_kb())