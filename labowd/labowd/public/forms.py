from django import forms
from public.models import *

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Peoples
        fields = "__all__"



