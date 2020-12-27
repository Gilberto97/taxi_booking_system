# taxi_booking_system

## Installation

```bash
git clone git@github.com:Gilberto97/taxi_booking_system.git
cd taxi_booking_system
virtualenv venv 
# or this instead: python -m virtualenv venv
source ./venv/bin/activate
pip install -r  requirements.txt
python manage.py migrate
```

## Running locally
```bash
python manage.py runserver
```

## Tests
```bash
python manage.py test
```
## Book-Trip
booking time must be in the following format:
year-month-day (make sure you put the dash in between elements)
