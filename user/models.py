from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from core.models import RefModel
from django.db import models
from django.core import exceptions
from rest_framework import serializers
from user.karfarmaModel import Karfarmamodel
from user.karjoModel import Karjomodel
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinValueValidator, MaxValueValidator
from models.messagesModel.models import Messagesmodel


class UserManager(BaseUserManager):
    
    def create_user(self, username, password, **extra_fields, ):
        
        """
        create user for project
        """
        
        extra_fields.setdefault("active", True)
        
        if not username:
            raise ValueError("Users must have an unique username")
        
        user = self.model(username=username, password=password, **extra_fields)
        
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.active = True
        user.is_admin = False
        
        user.full_clean()
        user.save(using=self._db)
        
        # find and set permission for user
        
        return user
        
    
    def create_superuser(self, username, password, **extra_fields, ):
        
        """
        create super user for django model
        """
        extra_fields.setdefault("is_superuser", True)
        
        user = self.create_user(username=username, password=password, **extra_fields)
        
        user.save(using=self._db)
        return user
        
    

class UsersType(models.IntegerChoices):
    SUPERUSER = 0, 'مدیر'
    KARFARMA_MODEL = 1, 'کارفرما'
    KARJO_MODEL = 2, 'کارجو'

class AllUsers(RefModel, AbstractBaseUser, PermissionsMixin):
    
    sms = models.IntegerField(verbose_name="اسمس", default=0)
    kifpool = models.IntegerField(verbose_name='کیف پول',default=0)
    username = models.IntegerField(validators=[
            MinValueValidator(9000000000),
            MaxValueValidator(9999999999)],
    unique=True, verbose_name="شماره تماس")
    usertype = models.IntegerField(choices=UsersType.choices, default=0, verbose_name="نوع کابر")
    active = models.BooleanField(default=True, verbose_name="فعال بودن اکانت")
    is_admin = models.BooleanField(default=False, verbose_name="کاربر ادمین")
    dataAccepted = models.BooleanField(default=False, verbose_name="اطلاعات تکمیل شده است")
    
    def __str__(self, *args, **kwargs):
        return str(self.username)
    
    def is_staff(self):
        return self.is_admin
    
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name_plural = "کاربران"
    
    
    @property
    def userdata(self):
        match self.usertype:
            case UsersType.KARFARMA_MODEL: return Karfarmamodel.objects.get(user_id=self.pk)
            case UsersType.KARJO_MODEL: return Karjomodel.objects.get(user_id=self.pk)
            case _: return self
    
    @property
    def notif(self):
        return Messagesmodel.objects.filter(user_id=self.pk)


class NotifSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Messagesmodel
        exclude = ["user"]
    

class UsersSerializer(serializers.ModelSerializer):
    
    notig = NotifSerializer(many=True)
    
    class Meta:
        model = AllUsers
        exclude = [
            "created_at",
            "password",
            "username",
            "is_superuser",
            "is_admin",
            "user_permissions",
            "groups",
            
        ]
    
    def validate(self, data):
        user = AllUsers(**data)
        password = data.get('password')
        print(data)
        if data["typeuser"] not in [0]:
            raise exceptions.ValidationError(
                {'error': 'user type is not valid'}
            )
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']}
            )
    
        return data
    
    def create(self, inputData):
        user = AllUsers.objects.create_user(
            username=inputData["username"],
            password=inputData["password"],
        )
        user.save()
        return user