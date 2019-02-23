from django.contrib import admin

# Register your models here.
from sx_user.models import UserModel, UserTicketModel, UserAddress


class UserModelAdmin(admin.ModelAdmin):
	fields = ("username", "password", "password_c", "email",)
	list_display = ("username", "email",)

class UserTicketModelAdmin(admin.ModelAdmin):
	fields = ("user", "ticket", "out_time",)
	list_display = ("ticket", "user", "out_time",)

class UserAddressAdmin(admin.ModelAdmin):
	fields = ("user", "recipients", "phone", "addressee_p", "direction",)
	list_display = ("user", "recipients", "phone", "addressee_p", "direction",)

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(UserTicketModel, UserTicketModelAdmin)
admin.site.register(UserAddress, UserAddressAdmin)

admin.site.site_header = "TTSX Admin"
admin.site.site_title = "TTSX"
