from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^.admin/', include(admin.site.urls)),

    url(r'^lookup/$', 'wedding.views.lookup', name='lookup'),
    url(r'^save/$', 'wedding.views.save', name='save'),
    url(r'', TemplateView.as_view(template_name='index.html')),
)
