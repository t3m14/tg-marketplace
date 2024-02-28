import config
import requests
import asyncio

from bot.keyboards.inline_keyboards import *

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

storage = MemoryStorage()

class cat_state(StatesGroup):
    select_cat = State()
    select_subcat = State()
    
bot = Bot(config.TOKEN)
dp = Dispatcher(storage=storage)



@dp.callback_query(cat_state.select_cat)
async def get_category_markup(call: types.CallbackQuery):
    category_list = []
    for i in Get_cat_markup().get_subcategories():
        if call.data in i["category"]["chapter"]["chapter_name"]:
            if types.InlineKeyboardButton(text=i["category"]["category_name"], callback_data=i["category"]["category_name"]) not in category_list:
                category_list.append(types.InlineKeyboardButton(text=i["category"]["category_name"], callback_data=i["category"]["category_name"]))
    if category_list != []:
        kb = types.InlineKeyboardMarkup()
        for btn in category_list:
            kb.add(btn)
        await cat_state.select_subcat.set()
        await call.message.edit_reply_markup(kb)
    else:pass
    
@dp.callback_query(cat_state.select_subcat)
async def get_subcategory_markup(call: types.CallbackQuery):
    subcategory_list = []
    for i in Get_cat_markup().get_subcategories():
        if call.data in i["category"]["category_name"]:
            
            subcategory_list.append(types.InlineKeyboardButton(text=i["subcategory_name"], callback_data=i["subcategory_name"]))
    kb = types.InlineKeyboardMarkup()
    for btn in subcategory_list:
        kb.add(btn)
    await call.message.edit_reply_markup(kb)
    
    
@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    
    kb = await get_chapter_markup()
    await state.set_state(cat_state.select_cat)
    await message.answer("Выберете нужное", reply_markup=kb)
    

async def start():
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    asyncio.run(start())