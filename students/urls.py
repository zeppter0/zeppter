from django.urls import path

from students.views import Dashboard, taxtnow

urlpatterns = [


    path("",Dashboard.as_view()),
    path("taxtnow",taxtnow.as_view()),



]