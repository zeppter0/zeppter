from django.urls import path

from myuser import views

urlpatterns = [
    path("register",views.Register,name="register"),
    path("login",views.login,name="login"),
    path('welcome',views.welcome ,name="welcome"),
    path('logout',views.logout ,name="logout"),
]