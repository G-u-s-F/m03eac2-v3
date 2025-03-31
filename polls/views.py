from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("<html><head><title>Hola mon</title></head><body><p>Hola mon, això és M03eac2.</p></body></html>")
