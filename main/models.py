from django.db import models
from django.utils import timezone

# Create your models here.
class System(models.Model):
    var = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.var}'
   

replied = [
    ('Yes', 'yes'),
    ('No', 'no')
] 
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    replied = models.CharField(max_length=100, choices=replied, default='No')
    
    def __str__(self):
        return f'{self.email} - {self.message}'
    
    
choices = [
    ('Male', 'male'),
    ('Female', 'female'),
    ('Other', 'other')
]
    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile_pics', default='default.jpg')
    gender = models.CharField(max_length=100, choices=choices, default='Male')
    education = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    bio = models.TextField()
    course = models.CharField(max_length=100, default='pcm')
    
    def __str__(self):
        return f'{self.name}'
    
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.IntegerField()
    subjects = models.CharField(max_length=300)
    seats_ava = models.CharField(max_length=100, choices=replied, default='No')
    
    def __str__(self):
        return f'{self.name}'
    
class Topper(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile_pics', default='default.jpg')
    course = models.ForeignKey(Course, related_name='toppers', on_delete=models.SET_DEFAULT, default='pcmb')
    batch = models.CharField(max_length=300)
    marks = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'
    
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers', default='default.jpg')
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title}'
    
    
class CollegeImage(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='col_images', default='default.jpg')
    
    def __str__(self):
        return f'{self.title}'
    
    
class Route(models.Model):
    locality = models.CharField(max_length=100)
    bus_no = models.IntegerField()
    fees = models.IntegerField()
    
    def __str__(self):
        return f'{self.locality}'