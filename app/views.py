from django.http import JsonResponse
from django.db import transaction
from django.db.models import QuerySet, Prefetch
from app.models import *

from os import environ as dotenv

DEBUG: bool = ( int(dotenv.get("DEBUG", "0")) != 0 )


def api_base():
    return JsonResponse({"status": "Api working."})


def get_version():
    return JsonResponse({"version": 1.0})
