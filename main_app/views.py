# main_app/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm


# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# HOME

class Home(LoginView):
    template_name = 'home.html'

def find_service_by_id(id):
    for service in services:
        if service.id == id:
            return service
    return None

# SERVICES
def service_index(request):
    return render(request, 'services/index.html', {'services': services})

def service_detail(request, service_id):
    service = find_service_by_id(service_id)
    return render(request, 'services/detail.html', {'service': service})

class Service:
    def __init__(self, type, description, cost, image, id):
        self.type = type
        self.description = description
        self.cost = cost
        self.image = image
        self.id = id
        

services = [
    Service(type='Blowout', description='', cost=40, image='images/blowout.png', id=1),
    Service(type='Womens Cut & Style', description='', cost=60, image='images/womenscutstyle.png', id=2),
    Service(type='Womens Master Cut & Style', description='', cost=65, image='images/mastercutstyle.png', id=3),
    Service(type='Mens Wash & Scissor Cut', description='', cost=40, image='images/menswashcut.png', id=4),
    Service(type='Lengthy Master Color', description='', cost=200, image='images/lengthmastercolor.png', id=5),
    Service(type='Buzz Master Color', description='', cost=100, image='images/buzzmastercolor.png', id=6),
    Service(type='Fix Your Face', description='Standard makeup', cost=60, image='images/fixyourface.png', id=7),
    Service(type='Face First', description='Master makeup', cost=90, image='images/facefirst.png', id=8),
]

#STYLISTS
# class Stylist:
#     def __init__(self, name, master, services, image):
#         self.name = name
#         self.master = master
#         self.services = services
#         self.image = image


# ABOUT
def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

# APPOINTMENTS
# @login_required
# def appointment_index(request):
#     my_appointments = request.user.appointment_set.all()
#     return render(request, 'myappointments.html', { 'myappointments': my_appointments })

class AppointmentCreate(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['service', 'stylist', 'date', 'time']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
@login_required    
def add_appointment(request, user_id):
    form = AppointmentForm(request.POST)
    if form.is_valid():
        new_appointment = form.save(commit=False)
        new_appointment.user_id = user_id
        new_appointment.save()
    return redirect('appointments.html')



class AppointmentUpdate(LoginRequiredMixin, UpdateView):
    model = Appointment
    fields = ['service', 'stylist', 'date', 'time']

class AppointmentDelete(LoginRequiredMixin, DeleteView):
    model = Appointment
    success_url = '/appointments'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('service-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})
