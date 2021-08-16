#page 48 TDD

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')