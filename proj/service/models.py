from django.db import models
class Service(models.Model):
    ser_icon= models.CharField(max_length=50)
    ser_title=models.CharField(max_length=50)
    ser_des=models.TextField()

# Create your models here.
