from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_page(request):
    form = UserCreationForm()
    context ={
        "form": form
    }
    if request.method == 'POST':
        form_data = UserRegisterationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "user account created successfully")
            return redirect('home')
    return render(request, "accounts/register.html", context)

def logout_confirm(request):

    return render(request, "accounts/logout_confirm.html")

@login_required
def profile_confirm(request):

    return render(request, "accounts/profile.html")