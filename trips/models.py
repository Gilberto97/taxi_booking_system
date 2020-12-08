from django.db import models
# from address.models import AddressField
from users.models import User, Driver

# Create your models here.

class Trip(models.Model):
    PAYMENT_METHODS = (
        ('1', 'Card'),
        ('2', 'Cash'),
    )
    customer = models.OneToOneField(User ,on_delete=models.CASCADE)
    pick_up_time = models.DateTimeField(blank=False, null=False)
    pick_up_place = models.CharField(max_length=80, blank=False, null=False)
    drop_off_place = models.CharField(max_length=80, blank=False, null=False)
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHODS)
    driver = models.OneToOneField(Driver , on_delete=models.CASCADE)

