from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from myadmin.admin import myadmin
from .models import User, ClientUser, ManagerUser, Address

# Register your models here.
@myadmin.ms_register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("title", "contact_name","email", "address_show")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "title",
                    "contact_name",
                    "contact_phone",
                    "province",
                    "city",
                    "district",
                    "place",
                    "email",
                    "is_default",
                ),
            },
        ),
    )
    # 两种方式 更新让用户界面只读的字段
    def get_readonly_fields(self, request, obj=None):
        readonly = super().get_readonly_fields(request, obj)
        if obj:
            readonly += ("user",)

        return readonly

    def address_show(self, obj):
        return f"{obj.province}{obj.city}{obj.district}{obj.place}"
    address_show.short_description = "地址"

    def changelist_view(self, request, extra_context=None):
        user_id = request.GET.get('user__id__exact')
        extra_context = extra_context or {}
        if user_id:
            try:
                user_obj = User.objects.get(id=user_id)
                extra_context["title"] = format_html(
                     '当前正在查看 <strong>{}</strong> 的地址列表',
                    user_obj.username
                )
            except User.DoesNotExist:
                pass
        return super().changelist_view(request, extra_context)

    #  用于给表单追加参数
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        user_id = request.GET.get('user__id__exact')
        if user_id:
            initial["user"] = user_id
        else:
            initial["user"] = "1"
        return initial

    # def save_model(self, request, obj, form, change):
    #     user_id = request.GET.get('user__id__exact')
    #     if user_id:
    #         user = User.objects.get(id=user_id)
    #         if not obj.user:
    #             obj.user = user
    #     super().save_model(request, obj, form, change)
    #
    # # get_form 可以调整表单渲染时的表现
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if obj is None:
    #         form.base_fields["user"].disabled = True
    #         form.base_fields['user'].required = False
    #         # form.base_fields['user'].widget.attrs['disabled'] = True
    #     return form

class ClientUserAdmin(UserAdmin):
    list_display = ("email", "nickname", "score", "is_active", "action_buttons")
    def action_buttons(self, obj):
        url  = reverse("admin:users_address_changelist") + f"?user__id__exact={obj.id}"
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
    myadmin.unregister(User)
except admin.sites.NotRegistered:
    pass

myadmin.register(ClientUser, ClientUserAdmin)
myadmin.register(ManagerUser, ManagerUserAdmin)
