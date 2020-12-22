from django.urls import path, include
from . import views


app_name = 'trips'
urlpatterns = [
    path('', views.index, name ='index'),
    path('book/', views.book_trip, name ='book'),
    path('trips/', views.trips, name ='trips'),
    
]