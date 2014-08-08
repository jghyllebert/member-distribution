from django.conf.urls import patterns, url

from .views import MemberCreateView, MemberDetailView, MemberListView

urlpatterns = patterns('',
    url(r'^add/$', MemberCreateView.as_view(), name='member_create'),
    url(r'^(?P<pk>[0-9]+)/$', MemberDetailView.as_view(), name='member_detail'),
    url(r'$', MemberListView.as_view(), name='member_list'),
)