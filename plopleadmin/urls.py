from django.urls import path

from plopleadmin import views

urlpatterns = [
    path("",views.index,name="home")
]