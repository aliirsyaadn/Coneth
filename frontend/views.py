from django.shortcuts import render, redirect

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

        os.system(
            f'echo "password" | sudo -S ./coneth.sh rename {current_name} {new_name}')

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

        return render(request, 'index.html', {"hopTo": "rename", "result_rename": new_name, 'device_name': device_name_stripped},)
    return redirect('index')


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
    return redirect('index')


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
    return redirect('index')


def set_device(request):
    if request.method == "POST":
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
    return redirect('index')


def info(request):
    if request.method == "POST":
        device = request.POST['device']

        os.system(f'./coneth.sh info {device} > result.txt')

        result = ""
        with open('result.txt', 'r') as file:
            result = file.read()

        os.system('./netdev.sh > device.txt')
        with open('device.txt', 'r') as file:
            device_name = file.readlines()

        device_name_stripped = []
        for name in device_name:
            device_name_stripped.append(name.strip())

        return render(request, 'index.html', {"hopTo": "info_device", "result_info": result, 'device_name': device_name_stripped})
    return redirect('index')


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
    return redirect('index')


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
    return redirect('index')


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
    return redirect('index')


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
    return redirect('index')
