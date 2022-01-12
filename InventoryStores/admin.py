from django.contrib import admin
from InventoryStores.models import Sale, StoreLocation


# Register your models here.

admin.site.register(StoreLocation)
admin.site.register(Sale)
