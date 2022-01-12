from django.urls import path, include
from .views import EquipmentListView
urlpatterns = [
    path('', EquipmentListView.as_view(), name ="Equipment List")
]
