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



        # withopen('result.txt', 'w') as file:


        # os.system('./coneth.sh rename {current_name} {new_name}')


    return render(request, 'index.html', {"hopTo": "rename", "result_rename": new_name},)


def version(request):
    if request.method == "POST":
        os.system('./coneth.sh version > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

    return render(request, 'index.html', {"hopTo": "version", "result_version": result})


def list_device(request):
    if request.method == "POST":
        os.system('./coneth.sh list > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()
    return render(request, 'index.html', {"hopTo": "list", "result_list": result})


def set_device(request):
    device = request.POST['device']
    speed = request.POST['speed']
    duplex = request.POST['duplex']
    auto_neg = request.POST['autoneg']
    os.system(f'./coneth.sh set {device} {speed} {duplex} {autoneg}')
    result = f"Device {device} was succesful to be set with speed of {speed} MB/s, {duplex} duplex, auto negotiation {autoneg}"
    return render(request, 'index.html', {"hopTo": "set_device", "result_set_device": result})


def info(request):
    if request.method == "POST":
        device = request.POST['device']

        os.system(f'./coneth.sh info {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        # result = "Settings for enp0s3:\n \
        # Supported ports: [ ]\n \
        # Supported link modes:   Not reported\n \
        # Supported pause frame use: No\n \
        # Supports auto-negotiation: No\n \
        # Supported FEC modes: Not reported\n \
        # Advertised link modes:  Not reported\n \
        # Advertised pause frame use: No\n \
        # Advertised auto-negotiation: No\n \
        # Advertised FEC modes: Not reported\n \
        # Speed: Unknown!\n \
        # Duplex: Unknown! (255)\n \
        # Port: Other\n \
        # PHYAD: 0\n \
        # Transceiver: internal\n \
        # Auto-negotiation: off\n \
        # Cannot get wake-on-lan settings: Operation not permitted\n \
        # Link detected: yes"


    return render(request, 'index.html', {"hopTo": "info_device", "result_info": result})


def infonet(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh infonet {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()
        


        
    return render(request, 'index.html', {"hopTo": "infonet_device", "result_infonet": result})


def down(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh down {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()


    return render(request, 'index.html', {"hopTo": "down", "result_down": result})


def up(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh up {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()
    return render(request, 'index.html', {"hopTo": "up", "result_up": result})


def speed(request):
    if request.method == "POST":
        os.system('./coneth.sh speed > result.txt')
        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()
    return render(request, 'index.html', {"hopTo": "speed", "result_speed": result})
