
from django.urls import path, include
from .views import *

app_name = "devtools"

urlpatterns = [
    path ('', main, name="main"),
    path ('create/', create, name="create"),
    path ('detail/<int:pk>/', detail, name="detail"),
    path ('delete/<int:pk>/', delete, name="delete"),
    path ('update/<int:pk>/', update, name="update"),
]