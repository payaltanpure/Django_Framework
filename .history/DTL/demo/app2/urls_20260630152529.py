from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('home_html/', views.home_html)
]
