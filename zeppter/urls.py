
from django.conf.urls import url
from django.contrib import admin



from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
path('hello/', include('admin_dashboard.urls')),
    path('', include('dashboard.urls')),
    path('json/', include('djson.urls')),
    path('comment/', include('comment.urls')),
    path("test/", include("mytest.urls")),
    path("call/", include('videocall.urls')),
    path("mobile/", include("mobile.urls")),
    path("test", include("mytest.urls")),
    path('teacher/',include('teacher.urls')),
    path('student/',include("students.urls")),

  #  url(r'^robots\.txt', TemplateView.as_view(template_name='include/robot.txt',
   #                                             content_type='text/plain')),
url('yandex_47dbe3c258eabd6f.html', TemplateView.as_view(template_name='include/yandex_47dbe3c258eabd6f.html',
                                                content_type='text/plain')),
    url('BingSiteAuth.xml',TemplateView.as_view(template_name='include/BingSiteAuth.xml',
                                                content_type='text/plain')),
    path("googleaec1d028d595b8d4.html" ,TemplateView.as_view(template_name='include/googleaec1d028d595b8d4.html',
                                                content_type='text/plain')),

# path("admin/<str:id>",include("plopleadmin.urls")),
    path("user/",include("myuser.urls")),
# path("robots.txt",views.robots ,name="roboot.txt"),


]

