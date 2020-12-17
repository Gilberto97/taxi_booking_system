from django.urls import path, include
from . import views

app_name = 'trips'
urlpatterns = [
    # Include default auth urls.
    path('', views.index, name ='index'),
    path('trips/', views.trips, name ='trips'),
]