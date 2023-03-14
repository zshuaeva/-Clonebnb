from django.db import models
from django.conf import settings
from django.urls import ...

class users():
  name = models.CharField(max_length=50)
  birthday = models.DateField(null=True, blank=True)
  photo = models.URLField()
  host_status = models.BooleanField()
  join_date = models.DateField()


#Ubiquitious Language:

# login form
# sign up form
# Rental creation form: will also contain amenity checklist form
# Booking
# Host
# Guest
# Reviews


class rentals():
  address = models.CharField()

#   FrontEnd:
# - BookingCreateForm.js (Guest)
# - RentalCreateForm.js (Host)
# - LoginInForm.js
# - SignUpForm.js

# - RentalList.js
# - RentalDetail.js
