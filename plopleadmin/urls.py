from django.urls import path

from plopleadmin import views

urlpatterns = [
    path("<str:id>",views.index,name="home")
]