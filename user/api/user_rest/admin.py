from django.contrib import admin
from user_rest.models import User, Amenity, Rental
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    pass
