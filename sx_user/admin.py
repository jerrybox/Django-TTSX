from django.contrib import admin

# Register your models here.
from sx_user.models import UserModel, UserTicketModel


class UserModelAdmin(admin.ModelAdmin):
	fields = ("username", "password", "password_c", "email", "recipients", "phone", "addressee_p", "direction",)
	list_display = ("username", "email", "phone",)

class UserTicketModelAdmin(admin.ModelAdmin):
	fields = ("user", "ticket", "out_time",)
	list_display = ("ticket", "user", "out_time",)


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(UserTicketModel, UserTicketModelAdmin)

admin.site.site_header = "TTSX Admin"
admin.site.site_title = "TTSX"
