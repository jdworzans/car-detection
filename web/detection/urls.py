from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detect-cars', views.detect_cars, name='detect-cars'),
]
