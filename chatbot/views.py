from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chatBot(req):
    return HttpResponse("Hello This is ChatBot")
