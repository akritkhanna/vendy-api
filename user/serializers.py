from rest_framework import serializers

from category.serializers import SubCategoriesSerializer
from location.serializers import LocationSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):

    sub_categories = SubCategoriesSerializer(many=True, read_only=True)
    current_location = LocationSerializer(many=False, read_only=True)
    avatar_url = serializers.SerializerMethodField('validate_avatar_url')
    # document_proof = serializers.SerializerMethodField('validate_document_url')

    class Meta:
        model = User
        # depth = 1
        fields = ['id', 'mobile_no', 'rating', 'name', 'avatar_url', 'is_vendor',
                  'business_name', 'business_description', 'is_admin', 'current_location', 'sub_categories']

    def validate_avatar_url(self, user):
        image = user.avatar_url
        if image:
            new_url = image.url
            if "?" in new_url:
                new_url = image.url[:image.url.rfind("?")]
            return new_url
        else:
            image = None
            return image


    # def validate_document_url(self, user):
    #     image = user.document_proof
    #     if image:
    #         new_url = image.url
    #         if "?" in new_url:
    #             new_url = image.url[:image.url.rfind("?")]
    #         return new_url
    #     else:
    #         image = None
    #         return image



class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['mobile_no', 'password', 'password2', 'name', 'avatar_url']
        extra_kwargs = {
            'password': {'write_only': True} #not to be shown in api view
        }

    def save(self):
        user = User(
            mobile_no=self.validated_data['mobile_no'],
            name=self.validated_data['name'],
            avatar_url=self.validated_data['avatar_url']
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
        fields = ['is_vendor', ]

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'is_sharing', 'business_description', 'business_name', 'current_location']

class VendorRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['sub_categories']





