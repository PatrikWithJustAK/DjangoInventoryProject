from django.contrib import admin
from InventoryEquipment.models import Equipment, EquipmentInstance, Transaction
# Register your models here.
admin.site.register(Equipment)
admin.site.register(EquipmentInstance)
admin.site.register(Transaction)