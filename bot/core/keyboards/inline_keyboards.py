from aiogram.utils.keyboard import InlineKeyboardBuilder

import requests
import core.config
from aiogram import types

worker_or_customer = InlineKeyboardBuilder()
worker_or_customer.row(
    types.InlineKeyboardButton(text="Фрилансер", callback_data="worker"),
    ).row(
        types.InlineKeyboardButton(text="Работодатель", callback_data="customer")
    )
    
cancel = InlineKeyboardBuilder()
cancel.row(
    types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    )
