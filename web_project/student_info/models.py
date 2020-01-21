from django.db import models

# Create your models here.
class Students(models.Model):

    name = models.CharField(max_length=300)
    student_num = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=100)
    email = models.CharField(max_length=100)