from django.shortcuts import render
from django.views import generic 
from .models import Equipment, EquipmentInstance
# Create your views here.

class EquipmentListView(generic.ListView):
    model = Equipment

class EquipmentInstanceListView(generic.ListView):
    model = EquipmentInstance
