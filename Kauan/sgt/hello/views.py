from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, world!")
def brian(request):
	return HttpResponse("Hello, Brian!")
def david(request):
	return HttpResponse("Hello, David!")
def greet(request, name):
	return HttpResponse(f"Hello, {name}!")
def index(request):
	return HttpResponse("<h1 style=\"color:green\">Hello, world!<h1>")
def index(request):
	return render(request, "hello/index.html")
