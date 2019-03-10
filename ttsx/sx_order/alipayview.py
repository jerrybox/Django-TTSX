"""
alipay views
"""

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse

from alipay.aop.api.util.SignatureUtils import verify_with_rsa

from ttsx.utils.functions import get_aliapy_client


def alipay_return(reqeust):
    """
    来自浏览器的同步消息
    return 支付成功提醒页，10秒后，然后跳转至订单页
    """
    return HttpResponseRedirect(reverse("order:user_center_order"))


@csrf_exempt
def alipay_notify(reqeust):
    """
    来自阿里服务器的异步消息，修改订单的状态
    """
    if request.method == 'POST':
        o_id = request.POST.get('out_trade_no')

        alipay_response = request.POST.dict()
        signature = alipay_response.pop("sign")
        alipay_response.pop('sign_type')
        response_dict = sorted(alipay_response.items(), key=lambda e: e[0], reverse=False)
        message = "&".join(u"{}={}".format(k, v) for k, v in response_dict).encode()
        success = False
        alipay_client = get_aliapy_client()
        try:
            success = verify_with_rsa(alipay_client.alipay_public_key, message, signature)
        except:
            success = False

        if success:
            user = reqeust.user
            order = OrderModel.objects.get_object_or_404(o_id=o_id)
            order.o_status = "Shipping"
            try:
                order.save()
            except:
                return False
