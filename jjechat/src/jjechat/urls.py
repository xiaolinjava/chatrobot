from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #project root default view
    url('^$', 'jjechat.books.views.index'),                   
    url(r'^index/$', 'jjechat.books.views.index', name="index"),
    url(r'^delete/(\d{1,10})/$', 'jjechat.books.views.delete', name="delete"),
    url(r'^edit/(\d{1,10})/$', 'jjechat.books.views.edit', name="edit"),
    url(r'^add/$', 'jjechat.books.views.add', name="add"),
    
    # Examples:
    # url(r'^$', 'jjechat.views.home', name='home'),
    # url(r'^jjechat/', include('jjechat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
