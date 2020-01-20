from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

from todo import views

urlpatterns = [
    url(r'^$', serve, kwargs={'path': 'index.html'}),
    url(r'^todos/$', views.TodoList.as_view()),
    path('admin/', admin.site.urls),
]

#    url(r'^$', serve, kwargs={'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)