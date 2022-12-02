from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loading, name="loading"),
    path('home', views.home, name="main-home"),
    path('admin-home', views.adminHome, name="main-admin"),
    path('admin-edit/<str:var>', views.adminEdit, name="admin-edit"),
    path('staff/new', views.newStaff, name='new-staff'),
    path('staff/<str:name>/edit', views.editStaff, name='edit-staff'),
    path('staff/<str:name>/delete', views.deleteStaff, name='delete-staff'),
    path('course/new', views.newCourse, name='new-course'),
    path('course/<str:name>/edit', views.editCourse, name='edit-course'),
    path('course/<str:name>/delete', views.deleteCourse, name='delete-course'),
    path('contacts/<str:message>/edit', views.replyView, name='edit-contacts'),
    path('staff/<str:name>/', views.staff, name="main-staff"),
    
    path('toppers/new', views.newTopper, name='new-topper'),
    path('toppers/<str:name>/edit', views.editTopper, name='edit-topper'),
    path('toppers/<str:name>/delete', views.deleteTopper, name='delete-topper'),
    
    path('events/new', views.newEvent, name='new-event'),
    path('events/<str:title>/edit', views.editEvent, name='edit-event'),
    path('events/<str:title>/delete', views.deleteEvent, name='delete-event'),
    
    path('images/new', views.newImage, name='new-image'),
    path('images/<str:title>/edit', views.editImage, name='edit-image'),
    path('images/<str:title>/delete', views.deleteImage, name='delete-image'),
    
    path('routes/new', views.newRoute, name='new-route'),
    path('routes/<str:locality>/edit', views.editRoute, name='edit-route'),
    path('routes/<str:locality>/delete', views.deleteRoute, name='delete-route'),
    
    path('system/<str:var>/edit', views.editSystem, name='edit-system'),
    
    path('events/', views.events, name="main-events"),
    path('routes/', views.routes, name="main-routes"),
    path('contact/', views.contactView, name="main-contact"),
    path('events/<str:title>/', views.eventInfo, name="event-info"),
    path('course/<str:title>/', views.courseInfo, name="main-course"),
    path('college-view/', views.collegeView, name="main-college"),
    path('college-view/<str:title>/', views.imageInfo, name="college-view"),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), 
         name='password_reset_complete'),
]