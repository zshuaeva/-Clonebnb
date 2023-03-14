from django.shortcuts import render
from django.http import JsonResponse
from common.json import ModelEncoder
import json
from django.views.decorators.http import require_http_methods
from .models import User
from .encoders import UserEncoder

@require_http_methods(["GET", "POST"])
def api_user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        return JsonResponse(
            {"users": users}, encoder=UserEncoder, safe=False
        )
    else:
        try:
            content = json.loads(request.body)
            user = User.objects.create(**content)
            return JsonResponse(
                {"Users": user}, encoder=UserEncoder, safe=False
            )
        except:
            response = JsonResponse({"message": "Invalid User Info"})
            response.status_code = 400
            return response
