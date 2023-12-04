from django.contrib import admin
from base.models import Car,Payments, Feedback

# Register your models here.

admin.site.register(Car)
admin.site.register(Payments)
admin.site.register(Feedback)