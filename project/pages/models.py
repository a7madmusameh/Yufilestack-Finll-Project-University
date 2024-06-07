
from django.db import models
from datetime import datetime
# Create your models here.

class Admins(models.Model):
    UserName = models.CharField(max_length=10)
    Password = models.CharField(max_length=50)
    def __str__(self):
        return self.UserName

class User(models.Model):
    username = models.CharField(max_length=10)
    Password = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Department(models.Model):
    Dname = models.CharField(max_length=25)
    name_file = models.CharField(max_length=50)
    index = models.TextField()
    files = models.FileField(upload_to='files/')
    path_file = models.CharField(max_length=50)
    def __str__(self):
        return self.name_file
class UserhasDep(models.Model):
    username = models.CharField(max_length=10)
    name_file = models.CharField(max_length=50)
    count_download = models.ImageField
    def __str__(self):
        return self.username 
class AdminsHasDep(models.Model):
    UserName = models.CharField(max_length=10)
    name_file = models.CharField(max_length=50)
    def __str__(self):
        return self.UserName
class search(models.Model):
    output =  models.TextField()
    date = models.DateTimeField(default=datetime.now)