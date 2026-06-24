from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class NewProductFSM(StatesGroup):
    subject = State()
    region = State()
    volume = State()
    price = State()
    
class EditProductFSM(StatesGroup):
    plan = State()
    option_to_edit = State()
    new_value = State()

class OrdersFSM(StatesGroup):
    id = State()
    