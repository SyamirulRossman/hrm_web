from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from dashboard_app.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated is False:
        return redirect('log_in')
    else:
        return redirect('dashboard')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged In Sucessfully!!")
                return redirect('dashboard')
            else:
                messages.error(request, "Wrong Credentials!!")
                return redirect('log_in')

    return render(request, 'log_in.html')

def log_out(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

@login_required
def dashboard(request):
    user = request.user
    full_name = user.first_name + " " + user.last_name

    users_in_system = get_user_model()
    users_in_system_count = users_in_system.objects.count()

    monthly_rent = Rent.objects.all()
    current_month = Rent.objects.last()
    rent_month = current_month.rent_month
    total = current_month.rent_amount + current_month.electric_amount + current_month.water_amount + current_month.wifi_amount + current_month.other_amount
    payment_person = round(float(total / users_in_system_count), 2)

    profiles = UserProfile.objects.get(user_id=user.id)
    all_profiles = UserProfile.objects.all()

    response_data = {
        "first_name": full_name,
        "monthly_rent": monthly_rent,
        "rent_month": rent_month,
        "total":total,
        "payment": payment_person,
        "profile": profiles,
        "all_profiles": all_profiles
    }

    return render(request, "dashboard.html", response_data)


def rent_view(request):
    monthly_rent = Rent.objects.all()
    currentmonth = Rent.objects.last()
    total = currentmonth.rent_amount + currentmonth.electric_amount + currentmonth.water_amount + currentmonth.wifi_amount + currentmonth.other_amount
    payment_person = round(float(total/3), 2)
    return render(request, 'rent.html', {"monthly_rent": monthly_rent, "total":total, "payment": payment_person})