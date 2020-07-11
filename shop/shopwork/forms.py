from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emplyee
        exclude = ('emp_join_date',)


