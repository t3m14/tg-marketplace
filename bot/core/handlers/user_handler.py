from aiogram import Router, F
from core.states.states import registration_state
from core.utils.database_operations import is_user_exists
from core.keyboards import inline_keyboards, reply_keyboards
from aiogram import types

router = Router()


@router.message(F.text == "/start")
async def start(message: types.Message):
    if is_user_exists(message.from_user.id):
        await message.answer("Привет! Пожалуйста, выбери действие", reply_markup=reply_keyboards.main_menu.as_markup())
    else:
        await message.answer("Привет! Давай заргестрируемся. Ты фрилансер или работодатель?", reply_markup=inline_keyboards.worker_or_customer.as_markup())
        await message.answer_photo(photo="AgACAgIAAxkBAANvZjzC5GwGXtDf5YztrLq1tRT-WFUAAqfaMRvjaelJ5_l4S_IK6z8BAAMCAAN5AAM1BA")

            