from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "detection/index.html")

def detect_cars(request):
    return HttpResponse("empty")
