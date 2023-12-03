from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact_number=models.IntegerField(max_length=11)   
    password=models.CharField(max_length=10)

    class Meta:
        db_table="user"

class Login(models.Model):
    email=models.CharField(max_length=100)  
    password=models.CharField(max_length=10)
