from django.contrib import admin

# Register your models here.
from sx_order.models import OrderModel, OrderDetailModel, Sales


class OrderModelAdmin(admin.ModelAdmin):
	fields = ("o_id", "o_user", "o_pay", "o_total", "o_address",)
	list_display = ("o_id", "o_user", "o_date", "o_pay", "o_total", "o_address",)


class OrderDetailModelAdmin(admin.ModelAdmin):
	fields = ("goods", "order", "price", "count", "isTrue",) 
	list_display = ("goods", "order", "price", "count", "isTrue",) 


class SalesAdmin(admin.ModelAdmin):
	fields = ("goods", "count", "total_price",)
	list_display = ("goods", "count", "total_price",)


admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(OrderDetailModel, OrderDetailModelAdmin)
admin.site.register(Sales, SalesAdmin)
