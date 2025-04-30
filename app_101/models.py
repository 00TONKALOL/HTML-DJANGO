from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


    class Meta:
        db_table = 'people'
