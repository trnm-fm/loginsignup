from django.db import models
from django.contrib.auth.models import (BaseUserManager ,AbstractBaseUser, PermissionsMixin)


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email , password , **extra_fields):
        
        if not email:
            raise ValueError(_("the Email must be set"))
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email , password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is False:
            raise ValueError(_('superuser must have is_staff=True'))
        

        if extra_fields.get('is_superuser') is False:
            raise ValueError(_('superuser must have is_superuser=True'))
        return self.create_user(email,password,**extra_fields)
     
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = []
    USERNAME_FIELD ='email'


    objects = UserManager()



    def __str__(self):
        return self.email
    

