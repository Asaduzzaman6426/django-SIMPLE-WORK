from django.urls import path
from . import views
app_name= 'fapp'
urlpatterns = [
    path("", views.home, name= "home"),
    path("v1/", views.eco, name= "view 1"),
]
