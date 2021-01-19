# taxi_booking_system

## Installation

```bash
cd taxi_booking_system
virtualenv venv 
# or this instead: python -m virtualenv venv
source ./venv/bin/activate
pip install -r  requirements.txt
python manage.py migrate
#create superuser
python manage.py createsuperuser
#additional command:
python manage.py migrate --run-syncdb

```

## Running locally
```bash
python manage.py runserver
```

## Tests
```bash
python manage.py test
```
