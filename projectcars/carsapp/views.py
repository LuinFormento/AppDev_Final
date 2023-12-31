from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Car_Model, Vehicle, AutoOrSemi, Classification, Logo
# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def vehicle_view(request):
    all_vehicle = Vehicle.objects.all()
    p = Paginator(all_vehicle, 5)
    page = request.GET.get('page')
    vehicle_list = p.get_page(page)
    return render(request, 'vehicle.html', {'vehicle': vehicle_list})

def logo_view(request):
    all_logo = Logo.objects.all()
    p = Paginator(all_logo, 5)
    page = request.GET.get('page')
    logo_list = p.get_page(page)
    return render(request, 'logo.html', {'logo': logo_list})

def Classification_view(request):
    all_project = Classification.objects.all()
    p = Paginator(all_project, 1)
    page = request.GET.get('page')
    classification_list = p.get_page(page)
    return render(request, 'project.html', {'project': classification_list})

def car_view(request):
    all_car_model = Car_Model.objects.all()
    p = Paginator(all_car_model, 5)
    page = request.GET.get('page')
    car_list = p.get_page(page)
    return render(request, 'position.html', {'position': car_list})

def autosemi_view(request):
    all_AoS = AutoOrSemi.objects.all()
    p = Paginator(all_AoS, 1)
    page = request.GET.get('page')
    AoS_list = p.get_page(page)
    return render(request, 'skill.html', {'skill': AoS_list})
