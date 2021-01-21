from django.urls import path

from myuser import views

urlpatterns = [
    path("register",views.Register,name="register"),
]