from django.contrib.admin import AdminSite

class MsAdminSite(AdminSite):
    site_header = "管理后台"
    site_title = "管理面板"
    index_title = "欢迎使用管理系统"

    def get_app_list(self, request, app_label = None):
        app_list = super().get_app_list(request, app_label)

        print(app_list)
        return app_list
