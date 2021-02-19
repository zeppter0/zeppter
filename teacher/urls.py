from django.urls import path
from teacher.views import Dashboard


urlpatterns = [


    path("",Dashboard.as_view()),


]