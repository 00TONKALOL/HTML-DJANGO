from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    weight = models.IntegerField(default=0)
    height = models.FloatField(default=1.6)
    gender = models.CharField(max_length=10, default="Male")
    salary=models.IntegerField(default=0)
    profile_pic=models.ImageField(upload_to="profile_pics", default="profile_pics/default.jpg")
    class Meta:
        db_table = 'people'
