from django.conf.urls import patterns, include, url

from TwiBibleApp.bible import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
