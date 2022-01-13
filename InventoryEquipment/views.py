from django.http import response
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views import generic 
from .models import Equipment, EquipmentInstance, Transaction
from InventoryStores.models import StoreLocation


# Create your views here.

class EquipmentListView(generic.ListView):
    model = Equipment

class EquipmentInstanceListView(generic.ListView):
    model = EquipmentInstance

class TransactionsListView(generic.ListView):
    model = Transaction

def LocationTransactionView(request, *args, **kwargs):

    pk= kwargs.get('pk')
    if pk:
        transactions = Transaction.objects.filter(store_location__StoreID=pk)
    else:
        transactions = Transaction.objects.filter(store_location__StoreID=2)

    context = {"Transactions": transactions}

    return render(request, "store_list.html", context)