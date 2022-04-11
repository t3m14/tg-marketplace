from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import api

urlpatterns = [
    path("chapters/", api.ChapterList.as_view()),
    path("categories/", api.CategoryList.as_view()),
    path("subcategories/", api.SubcategoryList.as_view()),
    path("posts/", api.PostList.as_view()),
]