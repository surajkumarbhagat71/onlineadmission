from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
admin.site.register(Product),
admin.site.register(Emplyee),
admin.site.register(DirSignup),