from django.urls import path
from feed.views import *

urlpatterns = [
    path('chapters/', ChaptersListView.as_view()),
    path('categories/', CategoriesListView.as_view()),
    path('categories/<int:chapter_id>/', CategoryByChapterListView.as_view()),
    path('subcategories/', SubcategoriesListView.as_view()),
    path('subcategories/<int:category_id>/', SubcategoryByCategoryListView.as_view()),
    path('services/', ServicesListCreateView.as_view()),
    # get services by subcategory
    path('services/<int:subcategory_id>/', ServicesBySubcategoryListView.as_view()),
    path('service/<int:pk>/', ServicesRetrieveUpdateDestroyView.as_view()),
    path('orders/', OrdedersListCreateView.as_view()),
    # get order by subcategory
    path('orders/<int:subcategory_id>/', OrdersBySubcategoryListView.as_view()),
    path('order/<int:pk>/', OrdersRetriveUpdateDestroyView.as_view()),
]