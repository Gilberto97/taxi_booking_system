from django.shortcuts import render, redirect
from django.http import HttpResponse
from trips.forms import InputForm
from django.contrib import messages 
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
    


