from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('{"response": "Synth is running!"}')


def test(request):
    return HttpResponse('ANOTHER RESPONSE YO')
