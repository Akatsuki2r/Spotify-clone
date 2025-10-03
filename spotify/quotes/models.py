from django.db import models

# Create your models here.
class Quote(models.Model):#This is the equivalent of creating a table in sql
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    
    #Incase we want to run this piece of code run the commands below
#python manage.py makemigrations
#python manage.py migrate
