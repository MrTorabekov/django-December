from django.shortcuts import render,HttpResponse

def home(requests):
    return HttpResponse("working django")
