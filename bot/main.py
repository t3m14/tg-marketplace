from select import select
from subprocess import call
from unicodedata import category
from urllib import response
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from aiogram import Bot, Dispatcher, types, executor
import config
import requests
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()

class cat_state(StatesGroup):
    select_cat = State()
    select_subcat = State()
    
bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=storage)

class Get_cat_markup():
    def get_chapters(self):
        chapters = requests.get("http://127.0.0.1:8000/chapters/").json()
        return chapters
    def get_categories(self):
        categories = requests.get("http://127.0.0.1:8000/categories/").json()
        return categories
    def get_subcategories(self):
        subcategories = requests.get("http://127.0.0.1:8000/subcategories/").json()
        return subcategories

async def get_chapter_markup():
    btns_list = []
    for i in Get_cat_markup().get_chapters():
        btns_list.append(types.InlineKeyboardButton(text=i["chapter_name"], callback_data=i["chapter_name"]))
    kb = types.InlineKeyboardMarkup()
    for btn in btns_list:
        kb.add(btn)
    await cat_state.select_cat.set()

    return kb

@dp.callback_query_handler(state=cat_state.select_cat)
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
    
@dp.callback_query_handler(state=cat_state.select_subcat)    
async def get_subcategory_markup(call: types.CallbackQuery):
    subcategory_list = []
    for i in Get_cat_markup().get_subcategories():
        if call.data in i["category"]["category_name"]:
            
            subcategory_list.append(types.InlineKeyboardButton(text=i["subcategory_name"], callback_data=i["subcategory_name"]))
    kb = types.InlineKeyboardMarkup()
    for btn in subcategory_list:
        kb.add(btn)
    await call.message.edit_reply_markup(kb)
    
    
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    
    kb = await get_chapter_markup()
    await message.answer("Выберете нужное", reply_markup=kb)
    


    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)