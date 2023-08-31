from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name



class Track(models.Model):
    track = models.CharField(max_length=256)
    
    def __str__(self):
        return self.track



class Enrollment(models.Model):
    subject = models.ManyToManyField(Subject)
    student = models.ManyToManyField(Student)
    teacher = models.ManyToManyField(Teacher)
    track = models.ManyToManyField(Track, blank=True)
    
    def __str__(self):
        return str(self.teacher)
