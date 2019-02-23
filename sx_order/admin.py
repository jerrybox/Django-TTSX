from django.contrib import admin

# Register your models here.
from sx_order.models import OrderModel, OrderDetailModel, Sales


class OrderModelAdmin(admin.ModelAdmin):
	fields = ("o_id", "o_user", "o_status", "o_total", "o_address",)
	readonly_fields = ("o_id", 'o_date_created', 'o_date_updated')
	list_display = ("o_user", "o_status", "o_total", "o_address",)


class OrderDetailModelAdmin(admin.ModelAdmin):
	fields = ("good_id", "order", "price", "count", "isTrue",) 
	readonly_fields = ("good_id", )
	list_display = ("order", "price", "count", "isTrue",) 


class SalesAdmin(admin.ModelAdmin):
	fields = ("goods", "count", "total_price",)
	list_display = ("goods", "count", "total_price",)


admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(OrderDetailModel, OrderDetailModelAdmin)
admin.site.register(Sales, SalesAdmin)
