import time
import random

from django.db import models
from django.utils.functional import cached_property
from django.core.exceptions import ObjectDoesNotExist

from sx_store.models import GoodsValue
from sx_user.models import UserModel


ORDER_STATUS_CHOICES= (
    ('NotPaid', '未支付'),
    ('Shipping', '运送中'),
    ('Shipped', '已收货'),
    ('Cancelled', '已取消'),
    ('Refunded', '已退款'),
    )


def generate_order_id():
    """
    生成唯一id用于订单号
    """
    chracter_num = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    now = time.gmtime()
    order_id = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday) + ''.join(random.choices(chracter_num, k=5))
    return order_id


class OrderModel(models.Model):
    """
    NOTE：订单的一些字段，不能使用外键关联，因为订单完成后，信息应该不能再改变
    TODO：
        保存订单时，生成一个唯一的order_id,用于提交支付
        送货地址，不应该是外键关系，不会随着外键关联对象的改变而改变
    """
    o_id = models.CharField(verbose_name="订单号",max_length=120, unique=True)        # 订单id
    o_user = models.ForeignKey(UserModel)                           # 关联用户
    o_date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)  # 创建日期
    o_date_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True)      # 支付日期
    o_status = models.CharField(max_length=120, default='NotPaid', choices= ORDER_STATUS_CHOICES)  # 付款属性
    o_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)   # 总价
    o_address = models.CharField(max_length=150, default="address")              # 收货地址
    o_freight = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.o_id = generate_order_id()
        super(OrderModel, self).save(*args, **kwargs)

    def __str__(self):
       return self.o_id

    class Meta:
        db_table = "sx_order"
        app_label = 'sx_order'
        verbose_name = '订单'
        verbose_name_plural = '订单'


# 创建订单详情表模型
class OrderDetailModel(models.Model):
    """
    NOTE:
        商品的价格会改变，因此，订单理记录价格不能使用外键
        注意如何精准计算
        这些外键字段应该存储商品的此时信息，且通过这个信息还能访问到商品的信息，类似edx里的course对象
    """
    good_id = models.IntegerField()     # 关联商品
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)        # 关联订单
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 总价
    count = models.IntegerField()                # 数量
    isTrue = models.BooleanField(default=False)  # 统计销量是否统计进去

    @cached_property
    def get_good(self):
        try:
            good = GoodsValue.objects.get(pk=self.good_id)
        except ObjectDoesNotExist:
            return "Off shelf"
        return good

    @cached_property
    def get_total(self):
        return self.price * self.count

    def __str__(self):
       return self.get_good.g_name

    class Meta:
        db_table = "sx_order_detail"
        app_label = 'sx_order'
        verbose_name = '订单条目'
        verbose_name_plural = '订单条目'


# 创建销量统计表模型
class Sales(models.Model):
    goods = models.ForeignKey(GoodsValue)    # 管理商品名称
    count = models.IntegerField()            # 销量
    total_price = models.DecimalField(max_digits=5, decimal_places=2)  # 销售额

    class Meta:
        db_table = "sx_sales"
        app_label = 'sx_order'
        verbose_name = '销量'
        verbose_name_plural = '销量'
