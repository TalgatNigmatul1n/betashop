from django.shortcuts import render
from django.http import HttpResponse

from .models import Products


def index(request):
    items = Products.objects.all()
    context = {
        'items': items
    }
    return render(request, 'betashop/index.html', context) 


def indexItem(request, id):
    item = Products.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'betashop/detail.html', context) 
