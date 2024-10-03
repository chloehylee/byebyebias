from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from django.http import JsonResponse

def apple_list(request):
    apples = Apple.objects.all()
    return JsonResponse(serialize_apples(apples), safe=False)

# def person_list(request):
#     persons = Person.objects.all()
#     return JsonResponse(serialize_persons(persons), safe=False)