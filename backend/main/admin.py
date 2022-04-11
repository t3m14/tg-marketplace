from django.contrib import admin
from . import models

class ChapterAdmin(admin.ModelAdmin):
    model = models.Chapter
class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category')
    model = models.Subcategory
class PostAdmin(admin.ModelAdmin):
    model = models.Post
    
admin.site.register(models.Chapter, ChapterAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Subcategory, SubcategoryAdmin)
admin.site.register(models.Post, PostAdmin)
