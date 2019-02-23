from django.conf.urls import url, include

from sx_order import views
from sx_order.alipayview import alipay_return, alipay_notify


ALIPAY_URLS = [
    url(r'^return/$', alipay_return, name='return'),
    url(r'^notify/$', alipay_notify, name='notify'),
]


urlpatterns = [
    # 提交订单
    url(r'^place_order/', views.place_order, name='place_order'),
    # 用户中心 - 用户信息页
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 用户中心 - 用户订单页
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 用户中心 - 用户收货地址页
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),
    # alipay 在线支付
    url(r'^alipay/', include(ALIPAY_URLS, namespace='aliapy')),
]

