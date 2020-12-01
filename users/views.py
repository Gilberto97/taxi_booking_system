from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# app imports
from .forms import CreateUserForm

def index(request):
    """This is the HomePage for Register/Log in"""
    dog = 'Bounty'
    context = {'dog': dog}
    return render(request, 'index.html', context)

def register(request):
    """Register a new user."""
    if request.method == 'GET':
        # Display blank registration form.
        form = CreateUserForm()
    else:
        # Process completed form.
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Welcome at our service ' + user)
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('users:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'register.html', context)
    
# Display login page only if users is already logged in.
# @login_required
# def account_view(request):
#     """ Update account details """

#     if not request.user.is_authenticated:
#         return redirect("login")
    
#     context = {}
    
#     if request.POST:
#         form = AccountUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.initial = {
#                 "email": request.POST['email'],
#                 "username": request.POST['username'],
#             }
#             form.save()
#             context['success_message'] = "Updated"
#     else:
        
#         form = AccountUpdateForm(

#             initial={
#                 "email": request.user.email,
#                 "username": request.user.username,
#             }
#         )
    
#     return render(request, "users/account.html", context)