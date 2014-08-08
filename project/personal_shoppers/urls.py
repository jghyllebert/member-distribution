from django.conf.urls import patterns, url
from personal_shoppers.views import PersonalShopperUpdateView

from .views import PersonalShopperCreateView, PersonalShopperDetailView, PersonalShopperListView

urlpatterns = patterns('',
    url(r'^add/$', PersonalShopperCreateView.as_view(), name='p_shopper_create'),
    url(r'^(?P<pk>[0-9]+)/$', PersonalShopperDetailView.as_view(), name='p_shopper_detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', PersonalShopperUpdateView.as_view(), name='p_shopper_update'),
    url(r'$', PersonalShopperListView.as_view(), name='p_shopper_list'),
)