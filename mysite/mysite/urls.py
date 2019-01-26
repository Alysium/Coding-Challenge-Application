from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path
from URL import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('URL.urls')),  
]







