from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "medalhas/index.html", {

    })
def brasil(request):
    return render(request, "medalhas/brasil.html", {

    })
def eua(request):
    return render(request, "medalhas/eua.html", {

    })

def franca(request):
    return HttpResponse("5 Medalhas de ouro.")
def japao(request):
    return HttpResponse("3 Medalhas de ouro.")
def china(request):
    return HttpResponse("2 Medalhas de ouro.")