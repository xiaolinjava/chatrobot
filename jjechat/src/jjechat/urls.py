from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#from jjechat.ot.views import index
from jjechat.books import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #project root default view
    url('^$', 'jjechat.ot.views.index'),                   
    #(r'^index/$', index),
    url(r'^index/$', 'jjechat.ot.views.index', name="index"),
    url(r'^index/(\d{1,2})/$', 'jjechat.ot.views.index', name="index"),
    url(r'^hello/$', 'jjechat.ot.views.hello', name='hello'),    
    
    (r'^books/index/$', views.index),               
    (r'^books/delete/(\d{1,10})/$', views.delete), 
    (r'^books/edit/(\d{1,10})/$', views.edit),
    (r'^books/add/$', views.add),
    # Examples:
    # url(r'^$', 'jjechat.views.home', name='home'),
    # url(r'^jjechat/', include('jjechat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
