from common.json import ModelEncoder
from .models import Amenity

class AmenityEncoder(ModelEncoder):
    model = Amenity
    properties = ["name", "category", "selected"]
