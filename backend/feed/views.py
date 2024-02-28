# generics crud
from rest_framework.views import APIView
from feed.models import Category, Subcategory, Chapter, Service, Order
from feed.serializers import CategorySerializer, SubcategorySerializer, ChapterSerializer, ServiceSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import generics


class ChaptersListView(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

# get category by chapter
class CategoryByChapterListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Category.objects.filter(chapter_id=chapter_id)

class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# get subcategory by category
class SubcategoryByCategoryListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Subcategory.objects.filter(category_id=category_id)


class SubcategoriesListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

# get services by subcategory
class ServicesBySubcategoryListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    def get_queryset(self):
        subcategory_id = self.kwargs['subcategory_id']
        return Service.objects.filter(subcategory_id=subcategory_id)

class ServicesListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServicesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# get orders by subcategory
class OrdersBySubcategoryListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_queryset(self):
        subcategory_id = self.kwargs['subcategory_id']
        return Order.objects.filter(subcategory_id=subcategory_id)

class OrdedersListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrdersRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
