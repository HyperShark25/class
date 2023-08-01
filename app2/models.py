from django.db import models
from django.contrib.auth import get_user_model
import random

UM = get_user_model()


class Student(models.Model):
    user = models.ForeignKey(UM, on_delete=models.CASCADE)
    fn = models.CharField(max_length=9, verbose_name="First Name")
    ln = models.CharField(max_length=8, verbose_name="Last Name")
    age = models.PositiveIntegerField(null=True)
    term = models.PositiveIntegerField(null=True)
    gpa = models.FloatField(null=True)
    
    def __str__(self):
        return self.reg_no
