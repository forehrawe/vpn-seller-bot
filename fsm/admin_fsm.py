from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class NewProductFSM(StatesGroup):
    subject = State()
    region = State()
    volume = State()
    price = State()
    