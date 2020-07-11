from django.db import models
from django.utils import timezone

# Create your models here.

class Director(models.Model):
    dir_id = models.AutoField(primary_key=True)
    dir_name = models.CharField(max_length=200)
    dir_email = models.EmailField()
    dir_password = models.CharField(max_length=200)
    dir_contact = models.IntegerField(default=0)

    def __str__(self):
        return self.dir_name

class College(models.Model):
    col_id = models.AutoField(primary_key=True)
    col_name = models.CharField(max_length=200)
    col_address = models.CharField(max_length=200)
    col_img = models.ImageField(upload_to='media')
    col_city = models.CharField(max_length=200)
    col_email = models.EmailField()
    col_contact = models.IntegerField(default=0)
    col_rank = models.IntegerField(default=0)

    def __str__(self):
        return self.col_name

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name

class Registation(models.Model):
    r_id  = models.AutoField(primary_key=True)
    student_first_name = models.CharField(max_length=200)
    student_last_name = models.CharField(max_length=200)
    student_address = models.CharField(max_length=200)
    student_email = models.EmailField(unique=True)
    student_contact = models.IntegerField()
    student_password = models.CharField(max_length=200)
    student_college_id = models.ForeignKey(College,on_delete=models.CASCADE)
    registation_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.student_first_name


class Admission(models.Model):
    admission_id = models.AutoField(primary_key=True)
    couse = models.ForeignKey(Course,on_delete=models.CASCADE)
    registation_no = models.ForeignKey(Registation,on_delete=models.CASCADE)
    admision_in_col = models.ForeignKey(College,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_img = models.ImageField(upload_to='media')
    GENDER = (("Male","Male",),("Fmale","Female"),("Other","Other"))
    genger = models.CharField(max_length=200,choices=GENDER)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    corrspondance_address = models.CharField(max_length=200)
    current_address = models.CharField(max_length=200)
    pass_out_class = models.CharField(max_length=200)
    passing_year = models.IntegerField(default=0)
    prasent_of_mark = models.IntegerField(default=0)
    admision_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.first_name


class Document(models.Model):
    d_id = models.AutoField(primary_key=True)
    marksit = models.ImageField(upload_to='media/')
    admit_card = models.ImageField(upload_to='media/')
    adhar_card = models.ImageField(upload_to='media/',default="")
    csc_or_slc = models.ImageField(upload_to="media/")
    student_id = models.ForeignKey(Registation,on_delete=models.CASCADE)