from django.urls import path, include
from .views import EquipmentListView, LocationTransactionView, EquipmentInstanceListView
urlpatterns = [
    path('', EquipmentListView.as_view(), name ="EquipmentList"),
    path('serials/', EquipmentInstanceListView.as_view(), name ="EquipmentInstanceList"),
    path('location/<int:pk>/', LocationTransactionView, name="StoreTransactions"),
    path('location/', LocationTransactionView, name="StoreTransactions",),
]
