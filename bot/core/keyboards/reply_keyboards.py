from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

main_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text="Лента")],
    [KeyboardButton(text="Профиль")],
    [KeyboardButton(text="Сделки")],
    [KeyboardButton(text="Настройки")]
])