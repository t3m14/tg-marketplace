from rest_framework import generics
from . import serializers
from . import models

class ChapterList(generics.ListAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
class CategoryList(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
class SubcategoryList(generics.ListAPIView):
    queryset = models.Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer
class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
