from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  name = models.CharField(max_length=50)
  birthday = models.DateField(null=True, blank=True)
  photo = models.URLField()
  host_status = models.BooleanField(default=False)
  join_date = models.DateField(null=True, blank=True, auto_now=True)

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
