from . import views
from django.urls import path

app_name = 'URLs'
urlpatterns = [

    path('', views.URL, name='URLhomepage'),
    path('<str:URLstr>/', views.URLstr, name='URLstr'),
]
