from django.db import models
from InventoryUsers.models import CustomUser
from InventoryEquipment.models import Equipment
import uuid
from django.utils import timezone
from django.utils.translation import gettext as _



# Create your models here.

class StoreLocation(models.Model):
    street_address = models.CharField(_("The Street Address"), max_length=50)
    zipcode = models.CharField(_("Zip Code Of the Location"), max_length=10)
    state = models.CharField(_("State of this location"), max_length=50)
    city = models.CharField(_("City of this location"), max_length=30)
    Address = models.CharField("Address of the location", max_length=50)
    Name = models.CharField("Common name for the store", max_length=50)
    Equipment = models.ManyToManyField("InventoryEquipment.Equipment", verbose_name=("Types of equipment this store keeps in stock"))
   # Manager = models.ForeignKey("app.Model", verbose_name=("The user object who manages this store"), on_delete=models.CASCADE) 
    StoreID = models.PositiveIntegerField(verbose_name="The ID of this store", primary_key=True)
    def __str__(self):
        return str(self.Name)


class Sale(models.Model):
    equipment = models.ForeignKey(Equipment, verbose_name=("Type of Equipment Sold"), on_delete=models.CASCADE)
   # user = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
   # customer = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    store_location = models.ForeignKey(StoreLocation, verbose_name=(""), on_delete=models.CASCADE)
    receipt = models.TextField(("Receipt Data"))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date_of_sale = models.DateTimeField("The time of the sale", auto_now=False, auto_now_add=False)
    equipment_instance = models.ForeignKey("InventoryEquipment.EquipmentInstance", verbose_name=_("The exact equipment sold"), related_name="EquipmentInstance", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)