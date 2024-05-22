from django.contrib import admin
from .models import *
# Register your models here.
class SingUpuser(admin.ModelAdmin):
    list_display = ('name','email','password','cpassword','option')

admin.site.register(SingUPform,SingUpuser)