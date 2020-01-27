from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from todo import views

urlpatterns = [
    url(r'^$', serve, kwargs={'path': 'index.html'}),

    url(r'^lookforit/$', views.LookForIt.as_view()),
    url(r'^lookforit/(?P<pk>[0-9]+)/$', views.LookForIt.as_view()),
    url(r'^pictures/(?P<pk>[0-9]+)/$', views.Pictures.as_view()),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)