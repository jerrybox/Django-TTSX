import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from django.db import transaction

from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest

from sx_shopping.models import CartInfo
from sx_user.models import UserModel
from sx_store.models import GoodsValue
from sx_order.models import  OrderModel, OrderDetailModel
from utils.functions import get_aliapy_client


# 提交订单
def place_order(request):
    """
    购物车选好商品后，创建订单，返回订单详情
    请求支付跳转
    取消订单
    """
    if request.method == 'GET':
        user = request.user

        # 从购物车获取订单信息
        goods_id_list = request.GET.get('goods_id_list', '')
        goods_id_list = json.loads(goods_id_list).get('goods_id', [])
        carts = CartInfo.objects.filter(user=user).select_related('goods')
        carts_list = []

        # 创建订单,一旦出错，回滚
        try:
            with transaction.atomic():
                # 创建订单
                order = OrderModel.objects.create(o_user=user)

                # 创建订单详情
                order_details = []
                for good_id in goods_id_list:
                    good_cart = carts.get(goods__id=good_id)
                    order_detail = OrderDetailModel.objects.create(
                                good_id=good_id, 
                                order=order, 
                                price=good_cart.goods.g_price, 
                                count =good_cart.count
                            )
                    order_details.append(order_detail)

                # 订单更新
                order.o_freight = 10
                order.o_total = sum([good.get_total for good in order_details])
                order.save()
        except Exception as e:
            return HttpResponse("出现错误....")

        # 创建支付链接
        alipay_client = get_aliapy_client()
        pay_model = AlipayTradePagePayModel()
        pay_model.out_trade_no = order.o_id
        pay_model.total_amount = order.o_total + order.o_freight
        pay_model.subject = "测试"
        pay_model.body = "支付宝测试"
        pay_model.product_code = "FAST_INSTANT_TRADE_PAY"
        alipay_request = AlipayTradePagePayRequest(biz_model=pay_model)
        aipay_url = alipay_client.page_execute(alipay_request, http_method="GET")

        cancel_url = ""
        data = {'carts': order_details,
                'aipay_url': aipay_url,
                "cancel_url": cancel_url
                }
        return render(request, 'place_order.html', data)



# 个人信息
def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


# 全部订单
def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'user_center_order.html')


# 收货地址
def user_center_site(request):
    # 拿到登陆用户的id
    id = request.user.id
    user_info = UserModel.objects.filter(id=id).first()
    if request.method == 'GET':
        data = {'user_info': user_info}
        return render(request, 'user_center_site.html', data)

    if request.method == 'POST':
        recipients = request.POST.get('recipients')
        direction = request.POST.get('direction')
        addressee_p = request.POST.get('addressee_p')
        phone = request.POST.get('phone')
        # 验证信息是否填写完整
        if not all([recipients, direction, addressee_p, phone]):
            data = {'msg': '请填写完整的收货信息!',
                    'user_info': user_info}  # 避免提交表单信息为空时当前地址不显示
            return render(request, 'user_center_site.html', data)
        user_info.recipients=recipients
        user_info.direction=direction
        user_info.addressee_p=addressee_p
        user_info.phone=phone
        user_info.save()
        data = {'msg': '收货地址添加成功'}
        return HttpResponseRedirect(reverse('order:user_center_site'), data)
