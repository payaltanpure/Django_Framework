from django.urls import path
from views import home

#create url
urlpatterns = [
    path('home/', home)
]
