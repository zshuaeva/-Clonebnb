from django.shortcuts import render
from django.http import JsonResponse
from common.json import ModelEncoder
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields import DateField
from django.views.decorators.http import require_http_methods
from .models import User
from .encoders import CustomJSONEncoder_User, UserEncoder


def user_to_json(user):
    return json.dumps(user, cls=UserEncoder)

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
