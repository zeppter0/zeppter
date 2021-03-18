from django.urls import path
from comment import views


urlpatterns = [
    path('',views.CommentPost.as_view() ),
    path('/send',views.send ,name="comment"),
]