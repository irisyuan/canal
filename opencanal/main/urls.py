from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
    # url(r'^$', 'opencanal.views.home', name='home'),
    # url(r'^opencanal/', include('opencanal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
    
    url(r'', include('application.urls')),
    url(r'', include('django.contrib.flatpages.urls')),

    url(r'^/application', include('application.urls')),
    url(r'^/application', include('registration.backends.default.urls')),
    
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^faq/$', 'flatpage', {'url': '/faq/'}, name='faq'),
    url(r'^termsofuse/$', 'flatpage', {'url': '/termsofuse/'}, name='termsofuse'),
    url(r'^privacy/$', 'flatpage', {'url': '/privacy/'}, name='privacy'),
    url(r'^resources/$', 'flatpage', {'url': '/resources/'}, name='resources'),
    url(r'^media/$', 'flatpage', {'url': '/media/'}, name='media'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()