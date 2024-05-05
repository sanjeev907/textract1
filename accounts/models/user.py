from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from accounts.models.country import Country 

class CustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



LOGIN_TYPE  = (('email', 'email'),('mobile','mobile'))

class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True,blank=True, unique= True)
    country_name = models.ForeignKey(Country, on_delete= models.CASCADE, related_name='user_country', blank=True, null=True,)
    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__(self):
        return self.email