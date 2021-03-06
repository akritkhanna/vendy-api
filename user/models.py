from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from vendy_api import settings


class MyUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, mobile_no, password=None):

        user = self.model(
            mobile_no=mobile_no,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, mobile_no, password):

        user = self.create_user(
            password=password,
            mobile_no=mobile_no,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):

    # CUSTOM FIELDS
    mobile_no = models.CharField(unique=True, max_length=10)
    rating = models.DecimalField(validators=[MaxValueValidator(5.0), MinValueValidator(0.0)],
                                 max_digits=3,
                                 decimal_places=2,
                                 default=0.0)

    name = models.CharField(max_length=20)
    avatar_url = models.ImageField(upload_to='profile_img/', default=None, blank=True, null=True)
    is_vendor = models.BooleanField(default=False)
    sub_categories = models.ManyToManyField('category.SubCategories', default=None, blank=True, null=True)
    current_location = models.OneToOneField('location.Location', on_delete=models.CASCADE, null=True, blank=True,  default=None)
    # has_applied = models.BooleanField(default=False)
    # document_proof = models.ImageField(upload_to='document_proof/', default=None, blank=True, null=True)
    business_name = models.CharField(max_length=30, default=None, blank=True, null=True)
    business_description = models.CharField(max_length=100, default=None, blank=True, null=True)
    is_sharing = models.BooleanField(default=False)

    # REQUIRED FIELDS (DON'T TOUCH)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last logined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_no'  # login field
    REQUIRED_FIELDS = []

    object = MyUserManager()

    def __str__(self):
        return self.mobile_no

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)