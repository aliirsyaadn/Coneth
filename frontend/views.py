from django.shortcuts import render

import os

# Create your views here.


def index(request):
    return render(request, 'index.html')


def rename(request):
    if request.method == "POST":
        print(request.POST['current-name'])
        print(request.POST['new-name'])

        current_name = request.POST['current-name']
        new_name = request.POST['new-name']

        os.system('./coneth.sh rename {current_name} {new_name}')

    return render(request, 'index.html', {"hopTo": "rename"})


def version(request):
    if request.method == "POST":
        os.system('./coneth.sh version')
    return render(request, 'index.html')


def list_device(request):
    if request.method == "POST":
        os.system('./coneth.sh list')
    return render(request, 'index.html')


def set_device(request):
    device = request.POST['device']
    speed = request.POST['speed']
    duplex = request.POST['duplex']
    auto_neg = request.POST['autoneg']
    os.system(f'./coneth.sh set {device} {speed} {duplex} {autoneg}')
    return render(request, 'index.html')


def info(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh info {device}')
    return render(request, 'index.html')


def infonet(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh infonet {device}')
    return render(request, 'index.html')


def down(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh down {device}')
    return render(request, 'index.html')


def up(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh up {device}')
    return render(request, 'index.html')


def speed(request):
    if request.method == "POST":
        os.system('./coneth.sh speed')
    return render(request, 'index.html')
