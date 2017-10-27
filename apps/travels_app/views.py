from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_app.models import User, UserManager
from .models import Trip, TripManager

# from .models import Task, TaskManager
import datetime

# Create your views here.
def dashboard(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'my_trips': Trip.objects.filter(users = User.objects.get(id=request.session['user_id'])),
        'trips': Trip.objects.exclude(users = User.objects.get(id=request.session['user_id']))

    }
    return render(request, 'travels_app/dashboard.html', context)



def create(request):
    print('================== "ADD VIEW"===================')
    return render(request, 'travels_app/trip.html')

def process(request):
    valid = Trip.objects.validate(request.POST, request.session['user_id'])
    if type(valid) == list:
        print('='*30)
        print(valid)
        for err in valid:
            messages.error(request, err)
        return redirect('travels:create')
    else: 
        return redirect('travels:dashboard')


def join(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    Trip.objects.get(id=trip_id).users.add(user)
    return redirect('travels:dashboard')


def destination(request, locale_id):
    trip = Trip.objects.get(id = locale_id)
    context = {
        'trip': trip,
        'notMe': trip.users.exclude(id=request.session['user_id'])
    }

    return render(request, 'travels_app/destination.html', context)