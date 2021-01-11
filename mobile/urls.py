from django.urls import path
from mobile import views



urlpatterns = [
    path("content/<int:id>/",views.content,name="content"),
    path("mobile_pdf/<int:id>",views.showdatapdf, name="showpdf"),
path("mobilecard/<int:id>",views.mobilecard, name="showpdf"),
    path("home",views.home,name="mobilehome"),
path("content/<int:id>/mobileload",views.content,name="contentload"),
    path("search",views.search,name="mobile_serach"),
    path("listview/<int:cat>",views.listview,name="listview"),
]