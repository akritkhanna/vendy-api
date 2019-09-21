from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Categories
from category.serializers import CategoriesSerializer

class CategoriesView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        categories = Categories.objects.all()

        categorySerializer = CategoriesSerializer(categories, many=True)
        content = {'categories': categorySerializer.data}
        return Response(content)
