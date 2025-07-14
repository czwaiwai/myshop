from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import User, ClientUser, ManagerUser, Address


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("title", "contact_name","email", "address_show")
    def address_show(self, obj):
        return f"{obj.province}{obj.city}{obj.district}{obj.place}"
    address_show.short_description = "地址"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user_id = request.GET.get("user_id")
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs

class ClientUserAdmin(UserAdmin):
    list_display = ("email", "nickname", "score", "is_active", "action_buttons")
    def action_buttons(self, obj):
        url  = reverse("admin:user-addresses", args=[obj.pk])
        return format_html('<a href="{}">{}</a>', url, "查看地址")
    action_buttons.short_description = '操作'

    search_fields = ("email", "nickname")
    list_filter = ("score",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "nickname",
                    "avator",
                    "score",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "nickname",
                    "avator",
                    "score",
                    "is_active",
                ),
            },
        ),
    )


    def get_readonly_fields(self, request, obj=None):
        readonly = super().get_readonly_fields(request, obj)
        if obj:
            readonly += ("email",)

        return readonly

    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type="client")


class ManagerUserAdmin(UserAdmin):
    # list_display = ("email", "nickname")
    search_fields = ("email", "nickname")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "nickname",
                    "is_active",
                ),
            },
        ),
    )
    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type="manager")


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(ClientUser, ClientUserAdmin)
admin.site.register(ManagerUser, ManagerUserAdmin)
