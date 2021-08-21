#page 108 TDD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})