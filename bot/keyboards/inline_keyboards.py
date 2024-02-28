from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests
import config
from aiogram import types
class Get_cat_markup():
    def get_chapters(self):
        chapters = requests.get(config.BACKEND_URL + "chapters/").json()
        return chapters
    def get_categories(self):
        categories = requests.get(config.BACKEND_URL + "categories/").json()
        return categories
    def get_subcategories(self):
        subcategories = requests.get(config.BACKEND_URL + "subcategories/").json()
        return subcategories


