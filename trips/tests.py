from django.test import TestCase
from datetime import date

from users.models import User, Customer, Driver, Company 
from .models import Trip 

class TripTestCase(TestCase):
    def setUp(self):

        company_user = User.objects.create_user(
            email='melani@study.beds.ac.uk', password='secret123', type=3)

        driver_user = User.objects.create_user(
            email='prem@study.beds.ac.uk', password='secret123', type=2)

        customer_user = User.objects.create_user(
            email='alex@study.beds.ac.uk', password='secret123', type=1)
        

        company = Company(user=company_user, phone_number="+441313131313", 
            name="Melani Ltd")
        company.save()

        driver = Driver(user=driver_user, phone_number="+441111111111",
            first_name="Prem", last_name="Kowalski", company=company)
        driver.save()

        customer = Customer(user=customer_user, phone_number="+441212121212", 
            first_name="Alex", last_name="Smith", card_number="1234123412341234", 
            ccv_number="123")
        customer.save()
        
        today = date.today()
        trip = Trip(customer=customer, pick_up_time=today, pick_up_place="Luton", drop_off_place="St. Albans", driver=driver)
        trip.save()

    def test_trip_created(self):

        trip = Trip.object.get(pick_up_place="Luton")
        print(trip)
        self.assertEqual(2,2)


