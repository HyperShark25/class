from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import random

def grn():
    return random.randint(0, 9999)


class Custom_User_Model(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    username = models.CharField(max_length=25, unique=True)
    form_id = models.IntegerField(default=grn, unique=True)
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.username
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
