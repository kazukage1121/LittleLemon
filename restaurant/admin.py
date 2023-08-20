from django.contrib import admin

# Register your models here.
from .models import Booking, MenuItem

admin.site.register(MenuItem)
admin.site.register(Booking)