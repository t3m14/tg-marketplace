from rest_framework import serializers
from . import models


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer()
    class Meta:
        model = models.Category
        fields = "__all__"


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Subcategory
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()
    class Meta:
        model = models.Post
        fields = "__all__"

        
