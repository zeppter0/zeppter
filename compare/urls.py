from django.urls import path

from compare import views

urlpatterns = [
    path('',views.Homw.as_view()),
    path('product',views.Product.as_view())
]