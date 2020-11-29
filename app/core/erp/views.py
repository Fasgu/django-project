from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from core.erp.models import Category
from core.erp.models import Product


def myFirstView(request):

    data = {
        'name': 'Aurora Soledad',
        'categories': Category.objects.all()
    }

    return render(request, 'index.html', data)

def mySecondView(request):

    data = {
        'name': 'Aurora Soledad',
        'products': Product.objects.all()
    }

    return render(request, 'second.html', data)