from django.urls import path

from . import views


urlpatterns = [
    path("", views.homepage , name="home-page"),
    path("getprofiles", views.getprofiles , name="getprofiles"),
    path("create", views.create , name="create"),
]