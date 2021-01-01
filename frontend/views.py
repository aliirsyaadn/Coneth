from django.shortcuts import render

import os

# Create your views here.


def index(request):

    os.system('./netdev.sh > device.txt')
    with open('device.txt', 'r') as file:
        device_name = file.readlines()

    device_name_stripped = []
    for name in device_name:
        device_name_stripped.append(name.strip())

    return render(request, 'index.html', {'device_name': device_name_stripped})


def rename(request):
    if request.method == "POST":
        print(request.POST['current-name'])
        print(request.POST['new-name'])

        current_name = request.POST['current-name']
        new_name = request.POST['new-name']

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

        # withopen('result.txt', 'w') as file:

        # os.system('echo "password" | sudo -S ./coneth.sh rename {current_name} {new_name}')

    return render(request, 'index.html', {"hopTo": "rename", "result_rename": new_name, 'device_name': device_name_stripped},)


def version(request):
    if request.method == "POST":
        os.system('./coneth.sh version > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

    return render(request, 'index.html', {"hopTo": "version", "result_version": result, 'device_name': device_name_stripped})


def list_device(request):
    if request.method == "POST":
        os.system('./coneth.sh list > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

    return render(request, 'index.html', {"hopTo": "list", "result_list": result, 'device_name': device_name_stripped})


def set_device(request):
    device = request.POST['device']
    speed = request.POST['speed']
    duplex = request.POST['duplex']
    auto_neg = request.POST['autoneg']
    os.system(
        f'echo "password" | sudo -S ./coneth.sh set {device} {speed} {duplex} {auto_neg}')
    result = f"Device {device} was succesful to be set with speed of {speed} MB/s, {duplex} duplex, auto negotiation {auto_neg}"

    os.system('./netdev.sh > device.txt')
    with open('device.txt', 'r') as file:
        device_name = file.readlines()

    device_name_stripped = []
    for name in device_name:
        device_name_stripped.append(name.strip())

    return render(request, 'index.html', {"hopTo": "set_device", "result_set_device": result, 'device_name': device_name_stripped})


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
        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

    return render(request, 'index.html', {"hopTo": "info_device", "result_info": result, 'device_name': device_name_stripped})


def infonet(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(f'./coneth.sh infonet {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

    return render(request, 'index.html', {"hopTo": "infonet_device", "result_infonet": result, 'device_name': device_name_stripped})


def down(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(
            f'echo "password" | sudo -S ./coneth.sh down {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()
        
        if len(result) < 3:
            result = "berhasil"

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())


    return render(request, 'index.html', {"hopTo": "down", "result_down": result, 'device_name': device_name_stripped})


def up(request):
    if request.method == "POST":
        device = request.POST['device']
        os.system(
            f'echo "password" | sudo -S ./coneth.sh up {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        if len(result) < 3:
            result = "berhasil"

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())
        
    return render(request, 'index.html', {"hopTo": "up", "result_up": result, 'device_name': device_name_stripped})


def speed(request):
    if request.method == "POST":
        os.system('./coneth.sh speed > result.txt')
        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())
    return render(request, 'index.html', {"hopTo": "speed", "result_speed": result, 'device_name': device_name_stripped})