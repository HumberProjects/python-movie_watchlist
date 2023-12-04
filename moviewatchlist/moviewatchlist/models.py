from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact_number=models.IntegerField(max_length=11)   
    password=models.CharField(max_length=10)

    class Meta:
        db_table="user"
        
class AddCategory(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    class Meta:
        db_table="category"
        
class AddMovie(models.Model):
    title=models.CharField(max_length=100)
    release_year=models.IntegerField(max_length=5)
    director=models.CharField(max_length=100)
    category_id=models.IntegerField(max_length=10)
    summary=models.CharField(max_length=255)
    rating=models.IntegerField(max_length=10)    
    class Meta:
        db_table="movie"

class Login(models.Model):
    email=models.CharField(max_length=100)  
    password=models.CharField(max_length=10)
