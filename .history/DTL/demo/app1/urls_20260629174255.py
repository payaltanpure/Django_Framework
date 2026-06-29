from django.urls import path
from . import views

#create url
urlpatterns = [
    path('home/', views.home),
    path('get_id/<int:id>',views.get_id),
    path('get_name/<string:name>', views.get_name),
]
