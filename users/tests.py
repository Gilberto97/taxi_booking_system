# importing TestCase - special build-in Django class to making tests
from django.test import TestCase

# importing models created in our 'users' app
from .models import User, Customer, Driver, Company 

# As we currently are in users app, below 'UserTestCase' will be used for testing
# its functionalities. 
# Please spend a few minutes and read about testing basics in Django:
# https://docs.djangoproject.com/en/3.1/topics/testing/overview/

class UserTestCase(TestCase):
    # 'setUp' is a special method to setting up our data before tests
    def setUp(self):
        # Creating all kind users, those base-users only stores email, password and user type info. 
        # We will use them for login into our app

        company_user = User.objects.create_user(
            email='melani@study.beds.ac.uk', password='secret123', type=3)

        driver_user = User.objects.create_user(
            email='prem@study.beds.ac.uk', password='secret123', type=2)

        customer_user = User.objects.create_user(
            email='alex@study.beds.ac.uk', password='secret123', type=1)
        
        # Creating specific users. 
        # Customer, Driver and Company models have got extended informations required for each user
        # type, but also reference (foreign key) to original user.
        # For each, firstable we provide all details, and then call '.save()' method to save it 
        # into database.

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

    # Let's check if users were created
    def test_users_created(self):
        # By 'Model.objects.get()' we can search specific records from database, so let's do it
        company = Company.objects.get(name="Melani Ltd")
        driver = Driver.objects.get(first_name="Prem")
        customer = Customer.objects.get(first_name="Alex")

        # Now let's check if all users exists
        are_users_created = bool(company) and bool(driver) and bool(customer)
        self.assertEqual(are_users_created, True)

    # We can also check if users can login with their provided email and password
    def test_users_can_login(self):
        # Django will handle login and return us a Boolean value if credentials are correct.
        is_company_logged = self.client.login(email='melani@study.beds.ac.uk', password='secret123')
        is_driver_logged = self.client.login(email='prem@study.beds.ac.uk', password='secret123')
        is_customer_logged = self.client.login(email='alex@study.beds.ac.uk', password='secret123')
        
        # Now let's check if all users exists
        are_users_logged = is_company_logged and is_driver_logged and is_customer_logged
        self.assertEqual(are_users_logged, True)
