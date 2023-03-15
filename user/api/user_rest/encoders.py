from common.json import ModelEncoder
from .models import User
from common.json import ModelEncoder
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields import DateField

class CustomJSONEncoder_User(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, DateField):
            return obj.strftime('%Y-%m-%d')
        if isinstance(obj, User):
            return {
                'id': obj.id,
                'photo': obj.photo,
                'email': obj.email,
                'host_status': obj.host_status,
                'username': obj.username,
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'birthday': obj.birthday,
                'password': obj.password,
                'is_superhost': obj.is_superhost
            }
        return super().default(obj)



from .models import User

class UserEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'id': obj.id,
                'username': obj.username,
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'email': obj.email,
                'birthday': obj.birthday,
                'photo': obj.photo,
                'host_status': obj.host_status,
                'is_superhost': obj.is_superhost
            }
        return super().default(obj)

# class UserEncoder(ModelEncoder):
#     model = User
#     properties = [
#         "id",
#         "name",
#         "birthday",
#         "photo",
#         "email",
#         "host_status",
#         "join_date",
#     ]
