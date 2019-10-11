from rest_framework import serializers
from .models import Categories, SubCategories


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['id', 'name', 'sub_types']


class SubCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategories
        fields = ['id', 'name']