from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def login(request):
    return HttpResponse('<h1> facualty login</h1>')

def registration(request):
    return HttpResponse('<h1> facualty registration</h1>')
def view_schedule(request):
    return HttpResponse('<h1> facualty schedule</h1>')
def view_feedback(request):
    return HttpResponse('<h1> view facualty feeback</h1>')
