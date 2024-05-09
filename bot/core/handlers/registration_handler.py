from aiogram import Router, F
from core.keyboards import inline_keyboards, reply_keyboards
from core.states.states import registration_state, menu_state
from core.config import API_URL
import aiohttp

from aiogram import types

router = Router()

# {
#   "name": "string",
#   "image": "string",
#   "description": "string",
#   "user_tag": "string",
#   "user_id": 9223372036854776000,
#   "rating": 9223372036854776000,
#   "portfolio_link": "string",
#   "role": "ADMIN"
# }
async def register_user(name, image, description, user_tag, user_id, role):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_URL}/users/register/", json={
            "name": name.strip(),
            "image": image,
            "description": description,
            "user_tag": user_tag,
            "user_id": user_id,
            "rating": rating,
            "portfolio_link": portfolio_link,
            "role": role
        }) as resp:
            return resp.status == 200


@router.callback_query(F.data == "customer")
async def customer_registration(callback: types.CallbackQuery, state: F.State):
    await callback.message.delete()
    await state.update_data(role=callback.data)
    await state.set_state(registration_state.set_portfolio)
    await callback.message.answer("Отправьте краткое описание вашего профиля", reply_markup=inline_keyboards.cancel.as_markup())


@router.callback_query(F.data == "worker")
async def worker_registration(callback: types.CallbackQuery, state: F.State):
    await callback.message.delete()
    await state.update_data(role=callback.data)
    await state.set_state(registration_state.set_description)
    await callback.message.answer("Отправьте краткое описание вашего профиля", reply_markup=inline_keyboards.cancel.as_markup())


@router.message(registration_state.set_description)
async def set_description(message: types.Message, state: F.State):
    await message.delete()
    await state.update_data(description=message.text)
    await state.set_state(registration_state.set_image)
    await message.answer("Отправьте фото вашего профиля", reply_markup=inline_keyboards.cancel.as_markup())


@router.message(registration_state.set_image, F.photo)
async def set_image(message: types.Message, state: F.State):
    await message.delete()
    photo = message.photo[-1].file_id
    data = await state.get_data()
    if await register_user(
        name=message.from_user.first_name + " " + message.from_user.last_name,
        image=photo,
        description=data['description'],
        user_tag=message.from_user.username,
        user_id=message.from_user.id,
        role=data['role'],
    ):
        await message.answer(
            f"Привет! Пожалуйста, выбери действие",
            reply_markup=reply_keyboards.main_menu.as_markup()
        )

        await state.set_state(menu_state.main_menu)
