from django.http import JsonResponse
import json

def getData(request):
    info = { "slackUsername": "@Kene4500", "backend": True, "age": 32, "bio": "I am in this program to upgrade my skillsets." }
    return JsonResponse(info, safe=False)