from common.json import ModelEncoder
from .models import User
from common.json import ModelEncoder

class UserEncoder(ModelEncoder):
    model = User
    properties = [
        "id",
        "name",
        "birthday",
        "photo",
        "host_status",
        "join_date",
    ]
