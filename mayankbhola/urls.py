from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mayankbhola.views.home', name='home'),
    # url(r'^mayankbhola/', include('mayankbhola.foo.urls')),

    #url(r'^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blogengine.views.date_archive', name="blog-date-archive"), 
    #url(r'^blog/archive/(?P<slug>[-\w]+)/$', 'blogengine.views.category_archive', name="blog-category-archive"),
    url(r'^blog/(?P<selected_page>\d+)/?$', 'blogengine.views.getPostsList'),
    url(r'^blog/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
    url(r'^blog/$', 'blogengine.views.getPostsList'),
	url(r'^admin/', include(admin.site.urls)),
)
