from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("persons/", views.PersonListView.as_view(), name="persons_list"),
]
