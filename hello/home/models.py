from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone= models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email

class Search(models.Model):
    search=models.CharField(max_length=200)


class Booking(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone= models.CharField(max_length=12)
    date=models.DateField()

    def __str__(self):
        return self.email




    
    

    
