from django.shortcuts import render, redirect
from django.http import HttpResponse
from trips.forms import InputForm
from django.contrib import messages 
from django.shortcuts import render
from .models import Trip
from datetime import datetime
from django.utils import timezone
import pytz




from users.models import User, Driver, Company 
# Create your views here.
def index(request):
    return render(request, 'trips/index.html')



def book_trip(request):
    form = InputForm(request.POST)
    if form.is_valid():

        event=form.save(commit=False)
        event.customer=request.user
        event.save()
        
    else:
        messages.error(request, "Error")
        
    return render(request, 'trips/book.html',{'form':form})
    

def trips(request):
    trips = Trip.objects.all()
    print(trips)
    context = {
        "trips_list": trips,
    }
    return render(request, 'trips/trips.html', context)

