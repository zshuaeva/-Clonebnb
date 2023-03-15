from django.shortcuts import render
from django.http import JsonResponse
from common.json import ModelEncoder
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields import DateField
from django.views.decorators.http import require_http_methods
from .models import User
from .encoders import UserEncoder, CustomJSONEncoder_User
from .models import Rental, Amenity



@require_http_methods(["GET", "POST"])
def api_user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        return JsonResponse(
            {"users": list(users)}, encoder=CustomJSONEncoder_User, safe=False
        )
    else:
        try:
            content = json.loads(request.body)
            user = User.objects.create(**content)
            return JsonResponse(
                {"users": user}, encoder=CustomJSONEncoder_User, safe=False
            )
        except:
            response = JsonResponse({"message": "Invalid User Info"})
            response.status_code = 400
            return response





class AmenityEncoder(ModelEncoder):
    model = Amenity
    properties = [
        "toilet_paper",
        "soap",
        "towels",
        "bedding",
        "cleaning_supplies",
        "pool",
        "wifi",
        "kitchen",
        "parking",
        "jacuzzi",
        "washer_dryer",
        "ac_heat",
        "self_check_in",
        "workspace",
        "pets_allowed",
        "carbon_monoxide_detector",
        "smoke_detector",
        "first_aid_kit",
        "fire_extinguisher",
        "step_free_access",
        "wide_entryway",
        "wide_hallway_clearance",
        "accessible_bathroom",
        "id",
    ]

class RentalEncoder(ModelEncoder):
    model = Rental
    properties = [
        "host",
        "address",
        "city",
        "state",
        "zip_code",
        "country",
        "id",
    ]
    encoders = {
        "amenities": AmenityEncoder(),
    }



@require_http_methods(["GET", "POST"])
def rental_list(request):
    if request.method == "GET":
        rentals = Rental.objects.all()
        return JsonResponse(
            list(rentals.values()),
            encoder=RentalEncoder,
            safe=False
        )

    elif request.method == "POST":
        data = json.loads(request.body)
        amenity_data = data.pop("amenities", None)
        rental = Rental.objects.create(**data)

        if amenity_data:
            amenity = Amenity.objects.create(rental=rental, **amenity_data)
            rental.amenities.add(amenity)

        return JsonResponse(
            rental,
            encoder=RentalEncoder,
            safe=False
        )

    else:
        return JsonResponse(
            {"error": "Invalid request method"},
            status=405
        )



@require_http_methods(["GET", "PUT", "DELETE"])
def rental_detail(request, id):
    try:
        rental = Rental.objects.get(id=id)
    except Rental.DoesNotExist:
        return JsonResponse(
            {"error": "Rental not found"},
            status=404
        )

    if request.method == "GET":
        return JsonResponse(
            rental,
            encoder=RentalEncoder,
            safe=False
        )

    elif request.method == "PUT":
        data = json.loads(request.body)
        amenity_data = data.pop("amenities", None)
        rental = Rental.objects.update(**data)

        if amenity_data:
            amenity = Amenity.objects.update(rental=rental, **amenity_data)
            rental.amenities.add(amenity)

        return JsonResponse(
            rental,
            encoder=RentalEncoder,
            safe=False
        )

    elif request.method == "DELETE":
        rental.delete()
        return JsonResponse(
            {"message": "Rental deleted"},
            status=204
        )

    else:
        return JsonResponse(
            {"error": "Invalid request method"},
            status=405
        )
