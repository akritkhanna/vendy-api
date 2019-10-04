from rest_framework import serializers

from category.serializers import CategoriesSerializer
from location.serializers import LocationSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):

    categories = CategoriesSerializer(many=True, read_only=True)
    current_location = LocationSerializer(many=False, read_only=True)
    avatar_url = serializers.SerializerMethodField('validate_avatar_url')
    document_proof = serializers.SerializerMethodField('validate_document_url')

    class Meta:
        model = User
        # depth = 1
        fields = ['id', 'mobile_no', 'rating', 'first_name', 'last_name', 'avatar_url', 'is_approved', 'has_applied',
                  'document_proof', 'is_admin', 'current_location', 'categories']

    def validate_avatar_url(self, user):
        image = user.avatar_url
        new_url = image.url
        if "?" in new_url:
            new_url = image.url[:image.url.rfind("?")]
        return new_url

    def validate_document_url(self, user):
        image = user.document_proof
        new_url = image.url
        if "?" in new_url:
            new_url = image.url[:image.url.rfind("?")]
        return new_url


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['mobile_no', 'password', 'password2', ]
        extra_kwargs = {
            'password': {'write_only': True} #not to be shown in api view
        }

    def save(self):
        user = User(
            mobile_no=self.validated_data['mobile_no'],
        )
        password = self.validated_data['password']
        password2 = self. validated_data['password2']


        if password != password2:
            raise serializers.ValidationError({'password': 'password should match'})
        user.set_password(password)
        user.save()
        return user

class UnapprovedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['is_approved', ]




