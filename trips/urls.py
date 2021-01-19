from django.urls import path, include
from . import views

app_name = 'trips'
urlpatterns = [
    # Include default auth urls.
    path('', views.index, name ='index'),
    path('about/', views.about, name ='about'),
    path('book/', views.book_trip, name ='book'),
    path('trips/', views.trips, name ='trips'),
    path('contact/', views.contact, name ='contact'),
    path('delete_trip/<int:id>/', views.delete_trip, name='delete-trip')

    
]