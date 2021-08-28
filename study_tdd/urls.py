from django.urls import path, include
from .views import *

app_name = 'english_teacher'
urlpatterns = [
    path('', index, name='index'),
    path('lists/new', new_list, name='new_list'),
    path('lists/one/', view_list, name='view_list'),

]

