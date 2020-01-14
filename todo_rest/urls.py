from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from rest_framework.urlpatterns import format_suffix_patterns

from todo import views

urlpatterns = [
    url(r'^$', serve, kwargs={'path': 'index.html'}),
    url(r'^todos/$', views.PictureView.as_view()),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),

]

#    url(r'^$', serve, kwargs={'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)