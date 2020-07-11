from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class RegForm(forms.ModelForm):
    class Meta:
        model = Registation
        exclude = ('registation_date',)

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ('student_id',)


class Admissionform(forms.ModelForm):
    class Meta:
        model = Admission
        exclude = ('admision_date','registation_no','admision_in_col')


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

