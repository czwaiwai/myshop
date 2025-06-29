from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ClientUser, ManagerUser


# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ("email", "username", "nickname", "is_active")
    search_fields = ("email", "nickname")
    list_filter = ("user_type", "is_staff")
    # fieldsets = (
    #     (
    #         None,
    #         {
    #             "fields": (
    #                 "username",
    #                 "password",
    #                 "nickname",
    #             ),
    #         },
    #     ),
    # )
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
                    "is_active",
                ),
            },
        ),
    )


class ClientUserAdmin(UserAdmin):
    list_display = ("email", "nickname", "score", "is_active")
    search_fields = ("email", "nickname")
    list_filter = ("score",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    # "email",
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

    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type="client")


class ManagerUserAdmin(UserAdmin):
    # list_display = ("email", "nickname")
    search_fields = ("email", "nickname")

    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type="manager")


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(ClientUser, ClientUserAdmin)
admin.site.register(ManagerUser, ManagerUserAdmin)
