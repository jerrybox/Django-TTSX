from django.db import models


# 创建用户信息模型
class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)      # 用户名
    password = models.CharField(max_length=256)                  # 密码
    password_c = models.CharField(max_length=256)                # 确认密码
    email = models.CharField(max_length=64, unique=True)         # 邮箱

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'sx_users'
        app_label = 'sx_user'
        verbose_name = '前台用户'
        verbose_name_plural = '前台用户'


class UserAddress(models.Model):
    """
    收货地址可以使用一套完全新：姓名，电话，邮件等信息
    """
    user = models.ForeignKey(UserModel)
    recipients = models.CharField(max_length=10, default='')     # 收件人姓名
    phone = models.CharField(max_length=11, default='')          # 收件人电话
    addressee_p = models.CharField(max_length=6, default='')     # 收件人邮编
    direction = models.CharField(max_length=100, default='')     # 收件人地址

    @property
    def complete_address(self):
        return self.recipients + self.phone + self.direction

    def __str__(self):
        return self.recipients + self.direction

    class Meta:
        db_table = 'sx_user_address'
        app_label = 'sx_user'
        verbose_name = '收货地址'
        verbose_name_plural = '收货地址'


# 创建用户Ticket模型
class UserTicketModel(models.Model):
    user = models.ForeignKey(UserModel)        # 关联用户模型
    ticket = models.CharField(max_length=256)  # 密码
    out_time = models.DateTimeField()          # 过期时间

    def __str__(self):
        return self.ticket

    class Meta:
        db_table = 'sx_users_ticket'
        app_label = 'sx_user'
        verbose_name = '用户Ticket'
        verbose_name_plural = '用户Ticket'
