from django.conf.urls import patterns, include, url

from django.contrib import admin
from members.views import MemberListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^personal_shoppers/', include('personal_shoppers.urls')),
    url(r'^members/', include('members.urls')),
    url(r'$', MemberListView.as_view(), name="home"),
)
