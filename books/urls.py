from django.urls import path

from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("books/<int:pk>", views.details, name="details"),
]