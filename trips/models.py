from django.db import models
# from address.models import AddressField
from users.models import Customer, User, Driver

# Create your models here.

class Trip(models.Model):
    customer = models.OneToOneField(Customer , on_delete=models.CASCADE)
    pick_up_time = models.DateTimeField(blank=False, null=False)
    pick_up_place = models.CharField(max_length=80, blank=False, null=False)
    drop_off_place = models.CharField(max_length=80, blank=False, null=False)
    driver = models.OneToOneField(Driver , on_delete=models.CASCADE)
