from django import forms
from django.contrib.auth.models import User
from .models import CollegeImage, Contact, Course, Event, Route, Staff, System, Topper

choices = [
    ('general', 'General'),
    ('action', 'Action'),
    ('romance', 'Romance')
]

class Seats(forms.Form):
    course = forms.CharField(max_length=100)
    
class SearchEvents(forms.Form):
    text = forms.CharField(max_length=200)
    
class Routes(forms.Form):
    route = forms.CharField(max_length=100)
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'profile', 'gender', 'education', 'subject', 'exp', 'bio', 'course']
        
        
class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message', 'replied']
        
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'fees', 'subjects', 'seats_ava']
        
        
class TopperForm(forms.ModelForm):
    class Meta:
        model = Topper
        fields = ['name', 'profile', 'course', 'batch', 'marks']
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'cover', 'description']
        
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = CollegeImage
        fields = ['title', 'cover']
        
        
class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['locality', 'bus_no', 'fees']
        
class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['var', 'value']
        
        
class DeleteField(forms.Form):
    agree = forms.BooleanField()