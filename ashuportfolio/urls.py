# ashuportfolio/urls.py
from django.contrib import admin
from django.urls import path
from home import views  # Import from 'home' app, not '.'

urlpatterns = [
    path('', views.my_view_home, name='my_view_home'),
    path('about/', views.my_view_about, name='my_view_about'),
    path('projects/', views.my_view_project, name='my_view_project'),
    path('contact/', views.my_view_contact, name='my_view_contact'),
    path('admin/', admin.site.urls),
]
