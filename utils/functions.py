import random
import os
import logging

from django.conf import settings

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient


logger = logging.getLogger(__name__)


def get_ticket():
    """
    仿随机的sessionid
    """
    ticket = ''
    s = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for x in range(100):
        ticket += random.choice(s)
    return ticket


def get_key_text(file_path):
    """
    读取keys文本
    """
    key_text = ''
    with open(file_path, 'r', encoding='UTF-8') as file:
        key_text = file.read()
    return key_text


def get_aliapy_client():
    """
    获取alipay配置参数，返回alipay client
    """
    alipay_client_config = AlipayClientConfig()

    if settings.PAYMENT_PROCESSOR_CONFIG['alipay']['mode'] == 'sandbox':
        alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    else:
        alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'

    alipay_client_config.app_id = settings.PAYMENT_PROCESSOR_CONFIG['alipay']['app_id']
    alipay_client_config.app_private_key =get_key_text(settings.PAYMENT_PROCESSOR_CONFIG['alipay']['app_private_key_path'])
    alipay_client_config.alipay_public_key = get_key_text(settings.PAYMENT_PROCESSOR_CONFIG['alipay']['alipay_public_key'])

    client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

    return client
    














