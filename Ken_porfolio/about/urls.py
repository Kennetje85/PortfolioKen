from django.urls import path
from . import views

urlpatterns = [
    path("", views.About_index, name="About_index"),
]