from rest_framework import serializers
from .models import Categories, SubCategories


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ['id', 'name']


class CategoriesSerializer(serializers.ModelSerializer):
    sub_types = SubCategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'sub_types']
