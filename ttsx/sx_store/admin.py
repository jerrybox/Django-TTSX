from django.contrib import admin

# Register your models here.
from ttsx.sx_store.models import ArticleCategory, GoodsValue


class ArticleCategoryAdmin(admin.ModelAdmin):
	fields = ("kind", "isDelete",)
	list_display = ("kind", "isDelete",)

class GoodsValueAdmin(admin.ModelAdmin):
	fields = ("g_name","g_img","g_num","g_price","g_unit","g_repertory","isDelete","gtype",)
	list_display = ("g_name","g_img","g_num","g_price","g_unit","g_repertory","isDelete","gtype",)


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(GoodsValue, GoodsValueAdmin)
