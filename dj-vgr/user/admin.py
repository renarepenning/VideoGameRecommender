from django.contrib import admin

# Register your models here.

from .models import myUser
admin.site.register(myUser) # insert ref to new table