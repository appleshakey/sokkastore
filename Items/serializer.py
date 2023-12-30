from rest_framework import serializers
from .models import Items, Category

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['identifier', 'name', 'description', 'price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'description']
