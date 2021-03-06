from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from cuba.views.accounts import UserCreateView
from settings import STATIC_ROOT
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
  (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes': True}),
  url(r'^$', TemplateView.as_view(template_name='index.html'), name='front_page'),
  url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
  url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
  url(r'^signup/$', UserCreateView.as_view()),
  url(r'^account/', include('cuba.urls.accounts')),
  url(r'^activity/', include('cuba.urls.activities')),
  #url(r'^activities/', include('cuba.urls.manage_activities')),
  url(r'^order/', include('cuba.urls.orders')),


  # Examples:
  # url(r'^$', 'cuba.views.home', name='home'),
  # url(r'^cuba/', include('cuba.foo.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
  url(r'^comments/', include('django.contrib.comments.urls')),
)
