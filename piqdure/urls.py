from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'piqdure.views.main', name='main'),
    url(r'^/?upperbar/?$', 'piqdure.views.upperbar', name='upperbar'),
    url(r'^/?pics/?$', 'piqdure.views.pics', name='pics'),
    # url(r'^piqdure/', include('piqdure.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
