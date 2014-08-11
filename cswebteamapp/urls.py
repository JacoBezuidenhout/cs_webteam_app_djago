from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cswebteamapp.views.home', name='home'),
    url(r'^microblog/', 'microblog.views.main', name='microblog'),
    url(r'^editpost/([0-9]*)$', 'microblog.views.editPost', name='editPost'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
