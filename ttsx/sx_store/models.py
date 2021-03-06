from django.db import models


# 创建商品种类模型
class ArticleCategory(models.Model):
    kind = models.CharField(max_length=30)            # 分类
    isDelete = models.BooleanField(default=False)     # 是否删除

    def __str__(self):
        return self.kind

    class Meta:
        db_table = "sx_kind"
        app_label = 'sx_store'
        verbose_name = '生鲜种类'
        verbose_name_plural = '生鲜种类'


# 创建商品属性模型
class GoodsValue(models.Model):
    """
    NOTE:用于历史订单要永久保留，不能删除商品，只能逻辑上下架
    """
    g_name = models.CharField(max_length=20)                  # 商品名称
    g_img = models.ImageField(upload_to='good')               # 商品图片
    g_num = models.CharField(max_length=100)                  # 商品货号
    g_price = models.FloatField(default=0)                    # 商品价格
    g_unit = models.CharField(max_length=20, default='500g')  # 商品单位
    g_repertory = models.IntegerField()                       # 商品库存
    isDelete = models.BooleanField(default=False)             # 是否删除，下架
    # 关联商品种类
    gtype = models.ForeignKey(ArticleCategory)

    def __str__(self):
        return self.g_name

    class Meta:
        db_table = "sx_goods"
        app_label = 'sx_store'
        verbose_name = '生鲜'
        verbose_name_plural = '生鲜'
