from django.shortcuts import render,redirect
from .forms import ContactForm, ContactForm2, CourseForm, DeleteField, EventForm, ImageForm, RouteForm, Routes, SearchEvents, Seats, StaffForm, SystemForm, TopperForm
from .models import CollegeImage, Contact, Course, Event, Route, Staff, System, Topper
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method == 'POST':
        u_form = Seats(request.POST)
        if u_form.is_valid():
            var = u_form.cleaned_data['course']
            return render(request, 'main/home.html', {'form':u_form, 'instagram':System.objects.filter(var="instagram").first(), 'facebook':System.objects.filter(var="facebook").first(), 'twitter':System.objects.filter(var="twitter").first(), 'address':System.objects.filter(var='address').first(), 'email':System.objects.filter(var='email').first(), 'phone_no':System.objects.filter(var='phone_no').first(), 'results':System.objects.all(), 'principal':Staff.objects.filter(subject="Principal").first(), 'staff':Staff.objects.exclude(subject="Principal").all(), 'toppers':Topper.objects.all(), 'events':Event.objects.order_by("-date_posted").all()[:3], 'images':CollegeImage.objects.all()[:3], 'title':'Home', 'desc':'JnanaGanga P.U. College, Nellikatte, the college of your dreams!'})
            
    else:
        u_form = Seats()
    
    return render(request, 'main/home.html', {'form':u_form, 'instagram':System.objects.filter(var="instagram").first(), 'facebook':System.objects.filter(var="facebook").first(), 'twitter':System.objects.filter(var="twitter").first(), 'address':System.objects.filter(var='address').first(), 'email':System.objects.filter(var='email').first(), 'phone_no':System.objects.filter(var='phone_no').first(), 'principal':Staff.objects.filter(subject="Principal").first(), 'staff':Staff.objects.exclude(subject="Principal").all(), 'toppers':Topper.objects.all(), 'events':Event.objects.order_by("-date_posted").all()[:3], 'images':CollegeImage.objects.all()[:3], 'title':'Home', 'desc':'JnanaGanga P.U. College, Nellikatte, the college of your dreams!'})



def staff(request, name):
    return render(request, 'main/staff.html', {'staff':Staff.objects.filter(name=name).first(), 'title':name})

def events(request):
    if request.method == 'POST':
        u_form = SearchEvents(request.POST)
        if u_form.is_valid():
            var = u_form.cleaned_data['text']
            return render(request, 'main/events.html', {'form':u_form, 'results':Event.objects.filter(title=var).order_by("-date_posted").all(), 'title':'Events'})
            
    else:
        u_form = SearchEvents()
    return render(request, 'main/events.html', {'form':u_form, 'events':Event.objects.order_by("-date_posted").all(), 'title':'Events'})

def routes(request):
    if request.method == 'POST':
        u_form = Routes(request.POST)
        if u_form.is_valid():
            var = u_form.cleaned_data['route']
            val = Route.objects.filter(locality=var).all()
            return render(request, 'main/routes.html', {'form':u_form, 'count':val.count, 'results':Route.objects.filter(locality=var).all(), 'title':'Routes'})
            
    else:
        u_form = Routes()
    return render(request, 'main/routes.html', {'form':u_form, 'title':'Routes'})


def eventInfo(request, title):
    return render(request, 'main/eventInfo.html', {'event':Event.objects.filter(title=title).first(), 'title':title})

def imageInfo(request, title):
    return render(request, 'main/imageInfo.html', {'image':CollegeImage.objects.filter(title=title).first(), 'title':title})

def courseInfo(request, title):
    if title == 'pcmc':
        choice = 'Biology'
        note = 'pcm'
    elif title == 'pcmb':
        choice = 'Computer Science'
        note = 'pcm'
    elif title == 'basc':
        choice = 'Economics'
        note = 'bas'
    elif title == 'base':
        choice = 'Computer Science'
        note = 'bas'
    return render(request, 'main/courseInfo.html', {'course':Course.objects.filter(name=title).first(), 'choice':choice, 'staff':Staff.objects.filter(course=note).exclude(subject=choice).all(), 'otherStaff':Staff.objects.filter(course='both').exclude(subject=choice).all(), 'title':title.upper})


def collegeView(request):
    if request.method == 'POST':
        u_form = SearchEvents(request.POST)
        if u_form.is_valid():
            var = u_form.cleaned_data['text']
            return render(request, 'main/collegeView.html', {'form':u_form, 'results':CollegeImage.objects.filter(title=var).all(), 'title':'Images'})
            
    else:
        u_form = SearchEvents()
    return render(request, 'main/collegeView.html', {'form':u_form, 'images':CollegeImage.objects.all(), 'title':'Images'})


def contactView(request):
    if request.method == 'POST':
        u_form = ContactForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"We have received your message! We'll get in touch with you as soon as possible.")
            return redirect('main-contact')
            
    else:
        u_form = ContactForm()
    return render(request, 'main/contact.html', {'form':u_form, 'title':'Contact'})


@login_required
def adminHome(request):
    return render(request, 'main/admin_home.html', {'title':'Admin'})

@login_required
def adminEdit(request, var):
    if var == 'staff':
        data = Staff.objects.all()
    elif var == 'contacts':
        data = Contact.objects.all()
    elif var == 'system':
        data = System.objects.all()
    elif var == 'course':
        data = Course.objects.all()
    elif var == 'toppers':
        data = Topper.objects.all()
    elif var == 'events':
        data = Event.objects.order_by("-date_posted").all()
    elif var == 'images':
        data = CollegeImage.objects.all()
    elif var == 'routes':
        data = Route.objects.all()
    else:
        data = ""
    return render(request, 'main/admin_edit.html', {'data':data, 'var':var})

@login_required
def newStaff(request):
    if request.method == 'POST':
        u_form = StaffForm(request.POST, request.FILES)
        if u_form.is_valid():
            staff = u_form.cleaned_data['name']
            u_form.save()
            messages.success(request, f"New Staff '{staff}' added!")
            return redirect('admin-edit', 'staff')
            
    else:
        u_form = StaffForm()
    return render(request, 'main/newStaff.html', {'form':u_form})


@login_required
def editStaff(request, name):
    if request.method == 'POST':
        u_form = StaffForm(request.POST, request.FILES, instance=Staff.objects.filter(name=name).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['name']
            u_form.save()
            messages.success(request, f"Staff '{staff}' edited successfully!")
            return redirect('admin-edit', 'staff')
            
    else:
        u_form = StaffForm(instance=Staff.objects.filter(name=name).first())
    return render(request, 'main/editStaff.html', {'form':u_form})

@login_required
def replyView(request, message):
    if request.method == 'POST':
        u_form = ContactForm2(request.POST, instance=Contact.objects.filter(message=message).first())
        if u_form.is_valid():
            u_form.save()
            return redirect('admin-edit', 'contacts')
            
    else:
        u_form = ContactForm2(instance=Contact.objects.filter(message=message).first())
    return render(request, 'main/replyView.html', {'form':u_form})



@login_required
def newCourse(request):
    if request.method == 'POST':
        u_form = CourseForm(request.POST)
        if u_form.is_valid():
            staff = u_form.cleaned_data['name']
            u_form.save()
            messages.success(request, f"New Course '{staff}' added!")
            return redirect('admin-edit', 'course')
            
    else:
        u_form = CourseForm()
    return render(request, 'main/newCourse.html', {'form':u_form})




@login_required
def editCourse(request, name):
    if request.method == 'POST':
        u_form = CourseForm(request.POST, instance=Course.objects.filter(name=name).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['name']
            u_form.save()
            messages.success(request, f"Course '{staff}' edited successfully!")
            return redirect('admin-edit', 'course')
            
    else:
        u_form = CourseForm(instance=Course.objects.filter(name=name).first())
    return render(request, 'main/editCourse.html', {'form':u_form})

@login_required
def deleteCourse(request, name):
    if request.method == 'POST':
        u_form = DeleteField(request.POST)
        if u_form.is_valid():
            agree = u_form.cleaned_data['agree']
            if agree == True:
                Course.objects.filter(name=name).first().delete()
            messages.success(request, f"Course '{name}' deleted successfully!")
            return redirect('admin-edit', 'course')
            
    else:
        u_form = DeleteField()
    return render(request, 'main/deleteCourse.html', {'form':u_form, 'name':name})


@login_required
def deleteStaff(request, name):
    if request.method == 'POST':
        u_form = DeleteField(request.POST)
        if u_form.is_valid():
            agree = u_form.cleaned_data['agree']
            if agree == True:
                Staff.objects.filter(name=name).first().delete()
            messages.success(request, f"Staff '{name}' deleted successfully!")
            return redirect('admin-edit', 'staff')
            
    else:
        u_form = DeleteField()
    return render(request, 'main/deleteCourse.html', {'form':u_form, 'name':name})




@login_required
def newTopper(request):
    if request.method == 'POST':
        u_form = TopperForm(request.POST, request.FILES)
        if u_form.is_valid():
            staff = u_form.cleaned_data['name']
            u_form.save()
            messages.success(request, f"New Topper '{staff}' added!")
            return redirect('admin-edit', 'toppers')
            
    else:
        u_form = TopperForm()
    return render(request, 'main/newTopper.html', {'form':u_form})


@login_required
def editTopper(request, name):
    if request.method == 'POST':
        u_form = TopperForm(request.POST, request.FILES, instance=Topper.objects.filter(name=name).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['name']
            u_form.save()
            messages.success(request, f"Topper '{staff}' edited successfully!")
            return redirect('admin-edit', 'toppers')
            
    else:
        u_form = TopperForm(instance=Topper.objects.filter(name=name).first())
    return render(request, 'main/editTopper.html', {'form':u_form})


@login_required
def deleteTopper(request, name):
    if request.method == 'POST':
        u_form = DeleteField(request.POST)
        if u_form.is_valid():
            agree = u_form.cleaned_data['agree']
            if agree == True:
                Topper.objects.filter(name=name).first().delete()
            messages.success(request, f"Topper '{name}' deleted successfully!")
            return redirect('admin-edit', 'toppers')
            
    else:
        u_form = DeleteField()
    return render(request, 'main/deleteCourse.html', {'form':u_form, 'name':name})






@login_required
def newEvent(request):
    if request.method == 'POST':
        u_form = EventForm(request.POST, request.FILES)
        if u_form.is_valid():
            staff = u_form.cleaned_data['title']
            u_form.save()
            messages.success(request, f"New Event '{staff}' added!")
            return redirect('admin-edit', 'events')
            
    else:
        u_form = EventForm()
    return render(request, 'main/newEvent.html', {'form':u_form})


@login_required
def editEvent(request, title):
    if request.method == 'POST':
        u_form = EventForm(request.POST, request.FILES, instance=Event.objects.filter(title=title).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['title']
            u_form.save()
            messages.success(request, f"Event '{staff}' edited successfully!")
            return redirect('admin-edit', 'events')

    else:
        u_form = EventForm(instance=Event.objects.filter(title=title).first())
    return render(request, 'main/editEvent.html', {'form':u_form})


@login_required
def deleteEvent(request, title):
    if request.method == 'POST':
        u_form = DeleteField(request.POST)
        if u_form.is_valid():
            agree = u_form.cleaned_data['agree']
            if agree == True:
                Event.objects.filter(title=title).first().delete()
            messages.success(request, f"Event '{title}' deleted successfully!")
            return redirect('admin-edit', 'events')
            
    else:
        u_form = DeleteField()
    return render(request, 'main/deleteCourse.html', {'form':u_form, 'name':title})



@login_required
def newImage(request):
    if request.method == 'POST':
        u_form = ImageForm(request.POST, request.FILES)
        if u_form.is_valid():
            staff = u_form.cleaned_data['title']
            u_form.save()
            messages.success(request, f"New Image '{staff}' added!")
            return redirect('admin-edit', 'images')
            
    else:
        u_form = ImageForm()
    return render(request, 'main/newImage.html', {'form':u_form})


@login_required
def editImage(request, title):
    if request.method == 'POST':
        u_form = ImageForm(request.POST, request.FILES, instance=CollegeImage.objects.filter(title=title).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['title']
            u_form.save()
            messages.success(request, f"Image '{staff}' edited successfully!")
            return redirect('admin-edit', 'images')

    else:
        u_form = ImageForm(instance=CollegeImage.objects.filter(title=title).first())
    return render(request, 'main/editImages.html', {'form':u_form})


@login_required
def deleteImage(request, title):
    if request.method == 'POST':
        u_form = DeleteField(request.POST)
        if u_form.is_valid():
            agree = u_form.cleaned_data['agree']
            if agree == True:
                CollegeImage.objects.filter(title=title).first().delete()
            messages.success(request, f"Image '{title}' deleted successfully!")
            return redirect('admin-edit', 'images')
            
    else:
        u_form = DeleteField()
    return render(request, 'main/deleteCourse.html', {'form':u_form, 'name':title})





@login_required
def newRoute(request):
    if request.method == 'POST':
        u_form = RouteForm(request.POST)
        if u_form.is_valid():
            staff = u_form.cleaned_data['locality']
            u_form.save()
            messages.success(request, f"New Route '{staff}' added!")
            return redirect('admin-edit', 'routes')
            
    else:
        u_form = RouteForm()
    return render(request, 'main/newRoute.html', {'form':u_form})




@login_required
def editRoute(request, locality):
    if request.method == 'POST':
        u_form = RouteForm(request.POST, instance=Route.objects.filter(locality=locality).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['locality']
            u_form.save()
            messages.success(request, f"Route '{staff}' edited successfully!")
            return redirect('admin-edit', 'routes')
            
    else:
        u_form = RouteForm(instance=Route.objects.filter(locality=locality).first())
    return render(request, 'main/editRoute.html', {'form':u_form})

@login_required
def deleteRoute(request, locality):
    if request.method == 'POST':
        u_form = DeleteField(request.POST)
        if u_form.is_valid():
            agree = u_form.cleaned_data['agree']
            if agree == True:
                Route.objects.filter(locality=locality).first().delete()
            messages.success(request, f"Route '{locality}' deleted successfully!")
            return redirect('admin-edit', 'routes')
            
    else:
        u_form = DeleteField()
    return render(request, 'main/deleteCourse.html', {'form':u_form, 'name':locality})


@login_required
def editSystem(request, var):
    if request.method == 'POST':
        u_form = SystemForm(request.POST, instance=System.objects.filter(var=var).first())
        if u_form.is_valid():
            staff = u_form.cleaned_data['var']
            u_form.save()
            messages.success(request, f"Variable '{staff}' edited successfully!")
            return redirect('admin-edit', 'system')
            
    else:
        u_form = SystemForm(instance=System.objects.filter(var=var).first())
    return render(request, 'main/editSystem.html', {'form':u_form, 'var':var})


def loading(request):
    return render(request, 'main/loading.html', {'title':'loading...', 'desc':'Loading...'})