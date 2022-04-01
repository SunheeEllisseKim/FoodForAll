# run python manage.py runserver on mysite dir
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # access the function index from views.py in home/ directory
]
