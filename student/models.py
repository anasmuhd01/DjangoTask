from django.db import models

# Create your models here.


class StudentDetails(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    div = models.CharField(max_length=100)
    year = models.IntegerField()
    img = models.ImageField(upload_to='stdentimage')
