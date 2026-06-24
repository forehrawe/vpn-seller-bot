from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.admin.admin import (
    admin_keyboard,
    manage_products, 
    back_to_products_panel_keyboard,
    options_to_edit_A,
    )
from keyboards.admin.admin import plans_list_A
from middlewares.admin_auth import AdminAuthentication
from database.models import Product
from database.config import SessionLocal
from fsm.admin_fsm import NewProductFSM, EditProductFSM
from callbacks.admin_callback import ProductCallback


product_router_A = Router()

product_router_A.message.middleware(AdminAuthentication())


# ==========================
# Product Main Handler
# ==========================

@product_router_A.message(F.text == "Manage Products 📦")
async def db_management(message: Message):
    await message.answer("Products Panel 📦", reply_markup=manage_products())


# ==========================
# Product Listing
# ==========================

@product_router_A.callback_query(F.data == "show_products_A")
async def show_products(callback: CallbackQuery):
    db = SessionLocal()
    products = db.query(Product).all()
    products_text = "\n".join(
    [
        f"id : {p.id}\n"
        f"📦 Subject: {p.subject}\n"
        f"🌍 Region: {p.region}\n"
        f"📏 Volume: {p.volume}GB\n"
        f"💰 Price: {p.price} Toman\n"
        for p in products
    ]
)
    await callback.message.edit_text(products_text, reply_markup=back_to_products_panel_keyboard())
    

# ==========================
# Product Creation
# ==========================

@product_router_A.callback_query(F.data == "new_product_A")
async def new_product(callback: CallbackQuery, state: FSMContext):
    await state.set_state(NewProductFSM.subject)
    await callback.message.edit_text("Enter a Subject For Your New Product")
    
@product_router_A.message(NewProductFSM.subject)
async def get_subject(message: Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(NewProductFSM.region)
    await message.answer("Enter Product's Region")
    
@product_router_A.message(NewProductFSM.region)
async def get_region(message: Message, state: FSMContext):
    await state.set_state(NewProductFSM.volume)
    await state.update_data(region=message.text)
    await message.answer("Enter Product's Volume in \"GB\"")
    
@product_router_A.message(NewProductFSM.volume)
async def get_volume(message: Message, state: FSMContext):
    await state.set_state(NewProductFSM.price)
    await state.update_data(volume=message.text)
    await message.answer("Enter Product's Price in \"Toman\"")
    
@product_router_A.message(NewProductFSM.price)
async def get_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    try:
        db = SessionLocal()
        product = Product(
            subject = data["subject"],
            region = data["region"],
            volume = data["volume"],
            price = data["price"]
                )
        
        db.add(product)
        db.commit()
        db.close()
        await message.answer("Product Added Successfully")
        await state.clear()
    except Exception as e:
        print(e)
        await message.answer("An Error Occurred❗ Please Try Again Later")
        
        

# ==========================
# Delete Product
# ==========================
    
@product_router_A.callback_query(F.data == "remove_product_A")
async def remove_product(callback: CallbackQuery):
    await callback.message.edit_text(
        "Enter Product To Remove",
        reply_markup=plans_list_A(action="delete"))
    
@product_router_A.callback_query(
    ProductCallback.filter(F.action == "delete"))
async def removoing(callback: CallbackQuery, callback_data: ProductCallback):
    try:
        db = SessionLocal()
        product = db.query(Product).filter(Product.id == callback_data.product_id).first()
        db.delete(product)
        db.commit()
        db.close()
        await callback.message.edit_text(
            "Successfully Deleted. ✅",
            reply_markup=back_to_products_panel_keyboard())
        
    except:
        await callback.message.edit_text(
            text="An Error Occurred❗ Please Try Again Later ",
            reply_markup=back_to_products_panel_keyboard()
            )
        

# ==========================
# Update Product
# ==========================
    
@product_router_A.callback_query(F.data == "update_products_A")
async def update_product(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Select a Product :", reply_markup=plans_list_A(action="update"))
    await state.set_state(EditProductFSM.plan)

@product_router_A.callback_query(ProductCallback.filter(F.action == "update"), EditProductFSM.plan)
async def get_product(callback: CallbackQuery, callback_data: ProductCallback, state: FSMContext):
    await state.update_data(plan=callback_data.product_id)
    await state.set_state(EditProductFSM.option_to_edit)
    await callback.message.edit_text("Which one do you want to edit?", reply_markup=options_to_edit_A())

@product_router_A.callback_query(EditProductFSM.option_to_edit)
async def get_option(callback: CallbackQuery, state: FSMContext):
    await state.update_data(option_to_edit=callback.data)
    print(callback.data)
    await state.set_state(EditProductFSM.new_value)
    await callback.message.edit_text("Enter New Value To Replace")

@product_router_A.message(EditProductFSM.new_value)
async def updating(message: Message, state: FSMContext):
    await state.update_data(new_value=message.text)
    data = await state.get_data()
    await state.clear()
    
    try:
        db = SessionLocal()
        product = db.query(Product).filter(Product.id==int(data["plan"])).first()
        option_to_edit = data["option_to_edit"]
        setattr(product, option_to_edit, data["new_value"])
        db.commit()
        db.close()
        
        await message.answer("Successfully Edited ✅")
    except:
        await message.answer(
            text="An Error Occurred❗ Please Try Again Later "
            )




# ==========================
# Back To Products Main Panel
# ==========================
@product_router_A.callback_query(F.data == "back_to_products_panel_A")
async def back_to_products_panel(callback: CallbackQuery):
    await callback.message.edit_text("Products Panel 📦", reply_markup=manage_products())
    