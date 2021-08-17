#page 98 TDD
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })