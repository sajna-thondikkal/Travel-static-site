from django.db import models

# Create your models here.
class dest(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='picture1')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class news(models.Model):
    image1=models.ImageField(upload_to='picture1')
    date=models.DateField()
    name1=models.CharField(max_length=200)
    desc1=models.TextField()

