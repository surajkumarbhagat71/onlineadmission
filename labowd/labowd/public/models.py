from django.db import models

# Create your models here.

class Categories(models.Model):
    cat_title = models.CharField(max_length=200)
    cat_description = models.TextField()
    cat_icon = models.CharField(max_length=25)
    cat_date_of_creation = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cat_title



CITY_CHOICE = [
    ("PRNA","Purnea"),
    ("PAT","Patna"),
]
STATE_CHOICE = [
    ("BR","Bihar"),
    ("JK","jharkhand"),
]

class Peoples(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Categories)
    contact = models.IntegerField(null=True)
    street = models.TextField()
    city = models.CharField(max_length=10,choices=CITY_CHOICE)
    state = models.CharField(max_length=10,choices=STATE_CHOICE)
    secondary_contact = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return (self.name)

