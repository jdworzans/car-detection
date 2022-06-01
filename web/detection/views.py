from django.http import HttpResponse
from django.shortcuts import render
import requests

from . import forms

def index(request):
    if request.method == "POST":
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            r = requests.get("http://torchserve:8080/predictions/fastrcnn", data=request.FILES['file'])
            results = r.json()
            car_results = filter(lambda entry: "car" in entry, results)
            return HttpResponse("valid")
        else:
            return HttpResponse("invalid")
    else:
        form = forms.UploadFileForm()
    return render(request, "detection/index.html")
