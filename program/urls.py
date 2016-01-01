from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from program import views

admin.autodiscover()

urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^programs/$', views.ProgramList.as_view()),
    url(r'^programs_detail/(?P<pk>[0-9]+)/$', views.ProgramDetail.as_view()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
