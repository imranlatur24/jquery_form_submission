from django.db import models

# Create your models here.
class Profile(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    class Meta:
        db_table="testing"