from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def myFirstView(request):
    data = {
        'name': 'Aurora Soldad'
    }
    return JsonResponse(data)