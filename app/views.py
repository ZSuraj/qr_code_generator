from django.shortcuts import render
from qrcode import *


# Create your views here.
def home(req):
    data = None
    qr_code_url = None
    if req.method == "POST":
        data = req.POST['data']

        img = make(data)
        img_path = f'app/static/images/{data.replace("://", "_").replace("/", "_")}.png'  # Create a valid filename
        img.save(img_path)
        qr_code_url = f'images/{data.replace("://", "_").replace("/", "_")}.png'

    else:
        print("else")

    return render(req, 'home.html', {"data": data, 'qr_code_url': qr_code_url},)
