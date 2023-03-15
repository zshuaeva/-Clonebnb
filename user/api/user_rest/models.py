from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
  name = models.CharField(max_length=50)
  birthday = models.DateField(null=True, blank=True)
  photo = models.URLField()
  email = models.EmailField(max_length=254, null=True)
  host_status = models.BooleanField(default=False)
  join_date = models.DateField(null=True, blank=True, auto_now=True)
  password = models.CharField(max_length=128, default=make_password(None))

  def __str__(self):
    return f"{self.name}"

#Ubiquitious Language:

# login form
# sign up form
# Rental creation form: will also contain amenity checklist form
# Booking
# Host
# Guest
# Reviews

#   FrontEnd:
# - BookingCreateForm.js (Guest)
# - RentalCreateForm.js (Host)
# - LoginInForm.js
# - SignUpForm.js

# - RentalList.js
# - RentalDetail.js
