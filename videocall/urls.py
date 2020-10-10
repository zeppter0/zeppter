from django.urls import path

from videocall import views

urlpatterns = [
    path('',views.data ,name="data")
]