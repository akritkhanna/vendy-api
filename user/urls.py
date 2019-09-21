from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


# router = routers.DefaultRouter()
# router.register('register', registration_view)
from user.views import UserView, UserRegistrationView, PendingUserApplication, ApproveUserApplicationView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    path('userlist', UserView.as_view(), name='userlist'),
    path('pendinglist', PendingUserApplication.as_view(), name='pendinglist'),
    path('approveuser/<int:id>', ApproveUserApplicationView.as_view(), name='approve_user'),

]