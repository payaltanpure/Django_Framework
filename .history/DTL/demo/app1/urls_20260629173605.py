from django.urls import path
from . import views

#create url
urlpatterns = [
    path('home/', views.home)
    path('get_id',views.get)
]
