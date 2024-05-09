"""
Models for the feed app.

Chapter: Chapter model representing a top-level category.
Category: Category model representing a sub-category under a chapter. Foreign key to Chapter.  
Subcategory: Subcategory model representing a sub-sub-category under a category. Foreign key to Category.

Service: Service model representing a service that can be offered. Has image, title, description, etc. Foreign key to Subcategory and User.
Order: Order model representing a request for work. Similar to Service. Foreign keys to Subcategory and User.

The models allow hierarchical categorization of services and orders, with foreign keys linking to subcategories.
"""
from django.db import models
from users.models import User

class Chapter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название главы')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Глава')
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    def __str__(self):
        return self.name

class Service(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_id = models.CharField(max_length=128, verbose_name="Айди картинки в телеграм")
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_top = models.BooleanField(default=False, verbose_name='Топ')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Работник')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    def __str__(self):
        return "Услуга + " + str(self.title)

class Order(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_id = models.CharField(max_length=128, verbose_name="Айди картинки в телеграм")
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    deadline = models.DateTimeField(verbose_name='Срок')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_top = models.BooleanField(default=False, verbose_name='Топ')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Работник')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    def __str__(self):
        return "Заказ + " + str(self.title)
