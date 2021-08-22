#page 123 TDD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one')
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})