from django.urls import path

from admin_dashboard import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
path('dashboard',views.shows,name="shows"),
    path('post',views.post, name='text'),
    path('addcategory',views.addcategory,name="adcategory"),
    path("delete/<int:id>",views.post_delele,name="post_delete"),
    path("cat_delete/<int:id>",views.cat_delete,name="catgory_delete"),
    path("post_update",views.post_update,name="post_update"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)