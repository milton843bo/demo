from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'add_user/$', 'home.views.add_user', name='add_user'),
    url(r'add_cita/$', 'home.views.add_cita', name='add_cita'),
    url(r'search/$', 'home.views.search_cita', name='search'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
