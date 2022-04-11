from django.db import models


class Chapter(models.Model):
    chapter_name = models.CharField(verbose_name="Имя раздела", max_length=64)
    def __str__(self):
        return self.chapter_name
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        
class Category(models.Model):
    category_name = models.CharField(verbose_name="Имя категории", max_length=64)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name="Раздел")
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
class Subcategory(models.Model):
    subcategory_name = models.CharField(verbose_name="Имя подкатегории", max_length=64)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    def __str__(self):
        return self.subcategory_name
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
class Post(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name="Подкатегория")
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.CharField(verbose_name="Описание", max_length=256)
    price = models.DecimalField(verbose_name="Цена", max_digits=1000, decimal_places=2)
    
    def __str__(self):
        return self.title + " " + str(self.price)
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"