from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Brasil/", views.brasil, name="brasil"),
    path("França/", views.franca, name="frança"),
    path("Argentina/", views.argentina, name="argentina")
]