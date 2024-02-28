from feed.models import *
from rest_framework import serializers
# import Resource

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    go_back = serializers.SerializerMethodField()
    def get_go_back(self, obj):
        return "/feed/chapters/"
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    go_back = serializers.SerializerMethodField()
    def get_go_back(self, obj):
        return "/feed/categories/" + str(obj.category.chapter.id)
    class Meta:
        model = Subcategory
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    go_back = serializers.SerializerMethodField()

    def get_go_back(self, obj): 
        return "/feed/subcategories/" + str(obj.subcategory.category.id)
    worker = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='WORKER'))
    class Meta:
        model = Service
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    go_back = serializers.SerializerMethodField()

    def get_go_back(self, obj): 
        return "/feed/subcategories/" + str(obj.subcategory.category.id)
    class Meta:
        model = Order
        fields = '__all__'