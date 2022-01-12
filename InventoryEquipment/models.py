from django.db import models
import uuid
from InventoryUsers.models import CustomUser
from django.utils import timezone
from django.utils.translation import gettext as _



# Create your models here.


class Equipment(models.Model):
    description = models.TextField("Description of the equipment")
    manufacturer = models.CharField("Who Makes this equipment?", max_length=50)
    model = models.CharField("Model of this equipment", max_length=50)

    def __str__(self):
        return str(self.model)


class EquipmentInstance(models.Model):
    LOCATION_STATUS = (
        ('OH', 'On Hand'),
        ('PT', 'Patient'),
        ('RC', 'Repair Center'),
        ('RT', 'Retired'),
        ('MIA', 'Missing In Action'),
    )
    EQUIPMENT_STATUS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    equipment = models.ForeignKey(Equipment, verbose_name=("Which type of equipment is this"), on_delete=models.CASCADE)
    serial_number = models.CharField(("Serial Number for this equipment"), max_length=50)
    isSold = models.BooleanField(default=False)
    arrived_date= models.DateField("Date the product was received", auto_now=False, auto_now_add=False)
    store_location= models.ForeignKey("InventoryStores.StoreLocation", verbose_name=("Location Equipment was delivered to"), on_delete=models.CASCADE)
    sale = models.ForeignKey("InventoryStores.Sale", verbose_name=("The Sale Data for when this was sold"), on_delete=models.CASCADE, null=True, blank=True)
    last_transaction_date = models.DateField(_("Date information was last modified"), auto_now=False, auto_now_add=True)
    location_status = models.CharField(_("Location Status Of Equipment"), max_length=3, choices=LOCATION_STATUS, default='OH')
    equipment_status = models.CharField(_("Equipment Status active/inactive/etc"), max_length=2, choices =EQUIPMENT_STATUS, default='A')
    current_customer_id = models.CharField(_("Customer ID of the customer who currently has possession of equipment"), max_length=50)
    meter_hours = models.PositiveIntegerField(_("Meter hours on the equipment"), null=True)
    next_pm_date = models.DateField(_("Date for next maintenance"), auto_now=False, auto_now_add=False)
    manager = models.ForeignKey(CustomUser, verbose_name=_("Manager responsible for this equipment"), on_delete=models.CASCADE)
    def __str__(self):
        return str(self.serial_number)

class Transaction(models.Model):
    
    equipment_instance = models.ForeignKey(EquipmentInstance, verbose_name=("The equipment that this transaction is for"), on_delete=models.CASCADE, blank=True)
    date_submitted = models.DateTimeField(_("When was this Transaction Submitted?"), auto_now=True, auto_now_add=True)
    date_approved = models.DateTimeField(_("When was this Transaction Approved?"), auto_now=False, auto_now_add=False, blank=True, null=True)
    serial_number = models.CharField(_("Serial Number for the associated Equipment"), max_length=50)
