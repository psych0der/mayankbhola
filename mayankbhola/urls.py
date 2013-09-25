from django.conf.urls import patterns, include, url
from django.views.generic.dates import ArchiveIndexView
from blogengine.views import PostsFeed
from blogengine.models import Post
from blogengine.views import PostYearArchiveView ,PostMonthArchiveView
from django.conf import settings
from django.conf.urls.static import static



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mayankbhola.views.home', name='home'),
    # url(r'^mayankbhola/', include('mayankbhola.foo.urls')),

    #url(r'^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blogengine.views.date_archive', name="blog-date-archive"), 
    
     

    url(r'^about/$', 'blogengine.views.aboutMe'),
    url(r'^projects/$', 'blogengine.views.projects'),
    url(r'^playground/$', 'blogengine.views.playground'),
    url(r'^contact/$', 'blogengine.views.contact'),

    url(r'^blog/archive/(?P<year>\d{4})/(?P<month>\d+)/$',
        PostMonthArchiveView.as_view(month_format='%m'),
        name="archive_month_numeric"),
    
    url(r'^blog/archive/(?P<year>\d{4})/(?P<month>[-\w]+)/$',
        PostMonthArchiveView.as_view(),
        name="archive_month"),

    url(r'^blog/category/(?P<categorySlug>[-\w]+)/(?P<selected_page>\d+)/?$', 'blogengine.views.getCategory'),
    url(r'^blog/category/(?P<categorySlug>[-\w]+)/$', 'blogengine.views.getCategory'),

    url(r'^blog/tag/(?P<tagSlug>[-\w]+)/(?P<selected_page>\d+)/?$', 'blogengine.views.getTag'),
    url(r'^blog/tag/(?P<tagSlug>[-\w]+)/$', 'blogengine.views.getTag'),
    
    url(r'^blog/\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
    url(r'^blog/(?P<selected_page>\d+)/?$', 'blogengine.views.getPostsList'),
    url(r'^blog/$', 'blogengine.views.getPostsList'),
    url(r'^feeds/posts/$', PostsFeed()),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blogengine.views.index'),
    
)

if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




