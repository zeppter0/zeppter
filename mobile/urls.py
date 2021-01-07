from django.urls import path
from mobile import views



urlpatterns = [
    path("content/<int:id>",views.content,name="content"),
    path("mobile_pdf/<int:id>",views.showdatapdf, name="showpdf"),
path("mobilecard/<int:id>",views.mobilecard, name="showpdf")
]