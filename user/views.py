from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer, UserRegistrationSerializer, UnapprovedUserSerializer


class UserView(APIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        query_set = User.object.all()
        # query_set = User.object.get(id=1)
        userSerializer = UserSerializer(query_set, many=True)
        content = {'users': userSerializer.data}
        return Response(content)


class UserRegistrationView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        user_register_serializer = UserRegistrationSerializer(data=request.data)

        data = {}
        if user_register_serializer.is_valid():
            user = user_register_serializer.save()
            data['response'] = 'success'
            data['mobile_no'] = user.mobile_no
            token = Token.objects.get(user=user).key
            data['token'] = token
            return Response(data)
        else:
            return Response(user_register_serializer.errors)


class PendingUserApplication(generics.ListAPIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAdminUser, ]

    queryset = User.object.all().filter(is_approved=False)
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['mobile_no', ]

    # def get(self, request, id, format=None):
    #     queryset = User.object.all().filter(is_approved=False)
    #     userSerializer = UserSerializer(queryset, many=True)
    #     content = {'unapproved_users': userSerializer.data}
    #     return Response(content)


class ApproveUserApplicationView(APIView):

    def put(self, request, id, format=None):
        unapproved_user = User.object.get(id=id)

        unapproveduserSerializer = UnapprovedUserSerializer(unapproved_user, data=request.data)

        data = {}

        if unapproveduserSerializer.is_valid():
            unapproveduserSerializer.save()
            data['response'] = 'Updated'
            data['user'] = unapproveduserSerializer.data
            return Response(data)
        else:
            return Response({'Error': 'Change me'})


