from django.contrib import admin
from .models import CollegeImage, Contact, Course, Event, Route, Staff, System, Topper

# Register your models here.
admin.site.register(System)
admin.site.register(Contact)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Topper)
admin.site.register(Event)
admin.site.register(CollegeImage)
admin.site.register(Route)