from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^search/$', views.search, name='search'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^wish/$', views.wish, name='wish'),
    url(r'^onsale/$', views.onsale, name='onsale'),
    url(r'^confirming/$', views.confirming, name='confirming'),
    url(r'^sale_request/$', views.sale_request, name='sale_request'),
    url(r'^sale_request_submitted/$', views.sale_request_submitted, name='sale_request_submitted'),
    url(r'^buy_request/$', views.buy_request, name='buy_request'),
    url(r'^buy_request_submitted/$', views.buy_request_submitted, name='buy_request_submitted'),
    url(r'^onsale_list/$', views.onsale_list, name='onsale_list'),
    url(r'^submitted_buy_request_list/$', views.submitted_buy_request_list, name='submitted_buy_request_list'),
    url(r'^edit_onsale/$', views.edit_onsale, name='edit_onsale'),
    url(r'^wish_list/$', views.wish_list, name='wish_list'),
    url(r'^edit_wish/$', views.edit_wish, name='edit_wish'),
    url(r'^submitted_sale_request_list/$', views.submitted_sale_request_list, name='submitted_sale_request_list'),
    url(r'^sell/$', views.sell, name='sell'),
    url(r'^sell_confirm/$', views.sell_confirm, name='sell_confirm'),
    url(r'^sell_completed/$', views.sell_completed, name='sell_completed'),
]
