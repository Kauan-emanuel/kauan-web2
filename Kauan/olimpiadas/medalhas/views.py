from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "medalhas/index.html", {

    })
def brasil(request):
    return render(request, "medalhas/brasil.html", {

    })
def brasil(request):
    return HttpResponse("7 Medalhas de ouro, 3 de prata e 2 de bronze.")
def franca(request):
    return HttpResponse("5 Medalhas de ouro.")
def argentina(request):
    return HttpResponse("3 Medalhas de ouro.")