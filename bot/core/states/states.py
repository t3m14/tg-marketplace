from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class registration_state(StatesGroup):
    set_description = State()
    set_image = State()
    set_portfolio = State()

class menu_state(StatesGroup):
    main_menu = State()
    profile_menu = State()
    deals_menu = State()
class cat_state(StatesGroup):
    select_cat = State()
    select_subcat = State()
