from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    pro_name = models.CharField(max_length=200)
    pro_code = models.IntegerField()
    pro_retail_price = models.IntegerField()
    pro_wholesale_price = models.IntegerField()

    def __str__(self):
        return self.pro_name


class Emplyee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    GENDER = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    emp_gender = models.CharField(choices=GENDER,max_length=200)
    emp_dob = models.DateField()
    emp_image = models.ImageField(upload_to='media/')
    emp_address = models.CharField(max_length=200)
    emp_city = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_password = models.CharField(max_length=200)
    emp_join_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.emp_name


class DirSignup(models.Model):
    dir_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email_id = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

