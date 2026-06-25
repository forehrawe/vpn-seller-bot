from aiogram import Router


order_router = Router()


# ==========================
# Orders Managing
# ==========================
# @product_router_A.message(F.text == "Show Order 🛒")
# async def show_order(message: Message, state: FSMContext):
#     await message.answer("Enter Order ID")
#     await state.set_state(OrdersFSM.id)

# @product_router_A