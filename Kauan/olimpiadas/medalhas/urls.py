from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Brasil/", views.brasil, name="brasil"),
    path("França/", views.franca, name="franca"),
    path("China/", views.china, name="china"),
    path("Japao/", views.japao, name="japao"),
    path("EUA/", views.eua, name="eua")
]