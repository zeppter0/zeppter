from django.urls import path

from admin_dashboard import views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('post',views.post, name='text')
]