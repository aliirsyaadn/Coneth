from django.urls import path

from .views import index, rename, version, list_device, set_device, info, infonet, down, up, speed

urlpatterns = [
    path('', index, name="index"),
    path('rename', rename, name="rename"),
    path('version', version, name="version"),
    path('list_device', list_device, name="list_device"),
    path('set_device', set_device, name="set_device"),
    path('info', info, name="info"),
    path('infonet', infonet, name="infonet"),
    path('down', down, name="down"),
    path('up', up, name="up"),
    path('speed', speed, name="speed"),
]
