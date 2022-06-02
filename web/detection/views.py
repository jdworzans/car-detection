import base64
import os
from io import BytesIO
from urllib.error import HTTPError

import requests
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image, ImageDraw

from . import forms


def save_img_to_response(img, response):
    with BytesIO() as buffer:
        img.save(buffer, "jpeg")
        buffer.seek(0)
        base64.encode(buffer, response)

def index(request):
    if request.method == "POST":
        form = forms.UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            r = requests.get(os.environ["PREDICTION_ADRESS"], data=request.FILES['file'])
            if r.ok:
                results = r.json()
                img = Image.open(request.FILES['file'])
                draw = ImageDraw.Draw(img)
                for result in filter(lambda entry: "car" in entry, results):
                    draw.rectangle(result["car"], outline=128, width=3)

                response = HttpResponse(content_type="image/jpeg", charset="utf-16")
                save_img_to_response(img, response)
                return response
            else:
                return HTTPError("Model not found", status=404)
        else:
            return HttpResponse("Validation of image failed.")
    return render(request, "detection/index.html")
