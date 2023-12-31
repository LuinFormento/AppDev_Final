from django.contrib import admin
from .models import Logo, Classification, AutoOrSemi, Car_Model, Vehicle

# Register your models here.
admin.site.register(Logo)
admin.site.register(Classification)
admin.site.register(AutoOrSemi)
admin.site.register(Car_Model)
admin.site.register(Vehicle)
