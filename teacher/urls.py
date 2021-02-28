from django.urls import path
from teacher.views import Dashboard,Works,worktext

urlpatterns = [


    path("",Dashboard.as_view()),
    path("works",Works.as_view()),
    path("worktext",worktext.as_view())



]