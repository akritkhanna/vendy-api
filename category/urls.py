from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


# router = routers.DefaultRouter()
# router.register('register', registration_view)
from category.views import CategoriesView

urlpatterns = [
    path('categories', CategoriesView.as_view(), name='categorylist'),

]