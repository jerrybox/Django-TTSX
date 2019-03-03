"""
alipay views
"""

from django.views.decorators.csrf import csrf_exempt

from alipay.aop.api.util.SignatureUtils import verify_with_rsa

from ttsx.utils.functions import get_aliapy_client


def alipay_return(reqeust):
	"""
	来自浏览器的同步消息
	return 支付成功提醒页，10秒后，然后跳转至订单页
	"""
	pass


@csrf_exempt
def alipay_notify(reqeust):
	"""
	来自阿里服务器的异步消息，修改订单的状态
	"""
	pass

