from django.db import models
from django.urls import reverse

# Create your models here.




class Amenity(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    selected = models.BooleanField(default=False)
    # rental = models.ForeignKey(
    #     "Rental",
    #     related_name="amenities",
    #     on_delete=models.PROTECT
    # )


    def __str__(self):
        return self.name


# class Rental(models.Model):
#     host = models.ForeignKey(
#         # User,
#         related_name="rental",
#         on_delete=models.PROTECT
#     )
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     zip_code = models.IntegerField()
#     country = models.CharField(max_length=255)
