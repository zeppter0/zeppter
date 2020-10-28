from django.urls import path

from admin_dashboard import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
path('dashboard',views.shows,name="shows"),
    path('post',views.post, name='text'),
    path('addcategory',views.addcategory,name="adcategory"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)