from django.urls import path, include

from . import views

# from .views import Home
app_name = "covidstatusapp"
urlpatterns = [
    path('', views.Home, name="home"),
    path('india', views.India, name="india"),

]
