from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>" , views.title, name="title"),
    path("add/", views.add, name="add"),
    path("search/", views.search , name="search"),
    path("edit/<str:title>", views.edit , name="edit"),
    path("convertir/<str:title>", views.convertir , name="convertir"),
    path("random/", views.random_entr, name="random")

]
