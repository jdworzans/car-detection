import requests
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image, ImageDraw

from . import forms


def index(request):
    if request.method == "POST":
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            r = requests.get("http://torchserve:8080/predictions/fastrcnn", data=request.FILES['file'])
            results = r.json()
            img = Image.open(request.FILES['file'])
            draw = ImageDraw.Draw(img)
            for result in filter(lambda entry: "car" in entry, results):
                print(result)
                draw.rectangle(result["car"], outline=128, width=3)
            img.save("out.jpg")
            return HttpResponse("valid")
        else:
            return HttpResponse("invalid")
    else:
        form = forms.UploadFileForm()
    return render(request, "detection/index.html")
