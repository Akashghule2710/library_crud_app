from django.db import models

class UserMaster(models.Model):
    firstname = models.TextField(max_length=10)
    lastname = models.TextField(max_length=10)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=50,unique=True)
    cpassword = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    #flags
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return self.firstname

class BookDetails(models.Model):
    bno = models.IntegerField()
    name = models.TextField(max_length=50)
    auther = models.TextField(max_length=50)
    status = models.TextField(max_length=50)
    
    