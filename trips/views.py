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
    # customer = User.objects.create_user(
    #     email='alex@study.beds.ac.uk', password='secret123', phone_number="+44121212112", 
    #     first_name="Alex", last_name="Smith")
    
    # company = Company(phone_number="+44131131313", name="Melani Ltd")
    # company.save()

    # driver = Driver(phone_number="+44111111", first_name="Prem", last_name="Kowalski", company=company, car_model="BWM", car_color="Black", car_license_plate="ABCD1234")
    # driver.save()

    # timezone.now()
    # today = datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)
    # trip = Trip(customer=customer, pick_up_time=today, pick_up_place="Luton", drop_off_place="St. Albans", payment_method='1', driver=driver)
    # trip.save()
    trips = Trip.objects.all()
    print(trips)
    context = {
        "trips_list": trips,
    }
    return render(request, 'trips/trips.html', context)

