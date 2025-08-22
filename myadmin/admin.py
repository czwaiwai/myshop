from django.contrib import admin


class MsAdminSite(admin.AdminSite):
    site_header = "管理后台"
    site_title = "管理面板"
    index_title = "欢迎使用管理系统"

    # 注册装饰器
    def ms_register(self, model):
        def wrapper(admin_class):
            self.register(model, admin_class)
            return admin_class

        return wrapper

    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request, app_label)

        # 使用 filter() 过滤掉 Address 模型
        filtered_app_list = []
        for app in app_list:
            # 用 filter 保留 object_name 不为 'Address' 的模型
            models = list(
                filter(lambda m: m["object_name"] != "Address", app["models"])
            )
            if models:
                app["models"] = models
                filtered_app_list.append(app)

        return filtered_app_list


myadmin = MsAdminSite(name="myadmin")
