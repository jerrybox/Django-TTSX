from django.contrib import admin

# Register your models here.
from ttsx.sx_shopping.models import CartInfo


class CartInfoAdmin(admin.ModelAdmin):
	fields = ("user", "goods", "count",)
	list_display = ("user", "goods", "count",)

admin.site.register(CartInfo, CartInfoAdmin)
