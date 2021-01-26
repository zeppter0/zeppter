from django.urls import path
from mobile import views



urlpatterns = [
    path("content/<str:title>/",views.content,name="content"),
    path("mobile_pdf/<int:id>",views.showdatapdf, name="showpdf"),
path("mobilecard/<int:id>",views.mobilecard, name="showpdf"),
    path("home",views.home,name="mobilehome"),
    path("content/<str:title>/mobileload",views.content,name="contentload"),
    path("search",views.search,name="mobile_serach"),
    path("listview/<int:cat>",views.listview,name="listview"),
]