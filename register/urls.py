from django.urls import path

from register import views


urlpatterns = [
    path("register",views.register,name="register"),
    path("upregister",views.upregister,name="uploa_data"),
    path("login",views.login,name="login")
]